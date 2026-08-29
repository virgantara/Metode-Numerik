"""Bab 2 - Visualisasi konvergensi metode pencarian akar.

File ini dibuat mandiri agar dapat langsung dijalankan dari folder bab02.
"""

import math
import numpy as np
import matplotlib.pyplot as plt


def biseksi(f, a, b, toleransi=1e-8, maks_iterasi=100):
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("Interval awal tidak memiliki perubahan tanda.")

    riwayat = []

    for k in range(1, maks_iterasi + 1):
        c = 0.5 * (a + b)
        fc = f(c)
        riwayat.append({"iterasi": k, "x": c, "residual": abs(fc)})

        if abs(fc) < toleransi or 0.5 * abs(b - a) < toleransi:
            return c, riwayat

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    raise RuntimeError("Biseksi belum konvergen.")


def regula_falsi(f, a, b, toleransi=1e-8, maks_iterasi=100):
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("Interval awal tidak memiliki perubahan tanda.")

    riwayat = []
    x_lama = None

    for k in range(1, maks_iterasi + 1):
        pembagi = fb - fa

        if abs(pembagi) <= math.ulp(1.0):
            raise ZeroDivisionError("Selisih nilai fungsi terlalu kecil.")

        x = b - fb * (b - a) / pembagi
        fx = f(x)
        riwayat.append({"iterasi": k, "x": x, "residual": abs(fx)})

        if abs(fx) < toleransi:
            return x, riwayat

        if x_lama is not None and abs(x - x_lama) < toleransi:
            return x, riwayat

        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        x_lama = x

    raise RuntimeError("Regula Falsi belum konvergen.")


def fixed_point(g, f, x0, toleransi=1e-8, maks_iterasi=100):
    x = float(x0)
    riwayat = []

    for k in range(1, maks_iterasi + 1):
        x_baru = g(x)
        residual = abs(f(x_baru))
        perubahan = abs(x_baru - x)
        riwayat.append(
            {
                "iterasi": k,
                "x": x_baru,
                "residual": residual,
            }
        )

        if residual < toleransi or perubahan < toleransi:
            return x_baru, riwayat

        x = x_baru

    raise RuntimeError("Iterasi Titik Tetap belum konvergen.")


def newton_raphson(f, df, x0, toleransi=1e-8, maks_iterasi=100):
    x = float(x0)
    riwayat = []

    for k in range(1, maks_iterasi + 1):
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-14:
            raise ZeroDivisionError("Turunan terlalu dekat dengan nol.")

        x_baru = x - fx / dfx
        residual = abs(f(x_baru))
        perubahan = abs(x_baru - x)
        riwayat.append(
            {
                "iterasi": k,
                "x": x_baru,
                "residual": residual,
            }
        )

        if residual < toleransi or perubahan < toleransi:
            return x_baru, riwayat

        x = x_baru

    raise RuntimeError("Newton-Raphson belum konvergen.")


def secant(f, x0, x1, toleransi=1e-8, maks_iterasi=100):
    f0 = f(x0)
    f1 = f(x1)
    riwayat = []

    for k in range(1, maks_iterasi + 1):
        pembagi = f1 - f0

        if abs(pembagi) <= math.ulp(1.0):
            raise ZeroDivisionError("Selisih nilai fungsi terlalu kecil.")

        x2 = x1 - f1 * (x1 - x0) / pembagi
        f2 = f(x2)
        residual = abs(f2)
        perubahan = abs(x2 - x1)
        riwayat.append(
            {
                "iterasi": k,
                "x": x2,
                "residual": residual,
            }
        )

        if residual < toleransi or perubahan < toleransi:
            return x2, riwayat

        x0, x1 = x1, x2
        f0, f1 = f1, f2

    raise RuntimeError("Secant belum konvergen.")


def f(x):
    return x**3 - x - 2


def df(x):
    return 3 * x**2 - 1


def g(x):
    return np.cbrt(x + 2)


def plot_riwayat(nama, riwayat):
    residual = [item["residual"] for item in riwayat]
    iterasi = range(1, len(residual) + 1)
    plt.semilogy(iterasi, residual, marker="o", label=nama)


if __name__ == "__main__":
    toleransi = 1e-8

    _, hist_b = biseksi(f, 1.0, 2.0, toleransi)
    _, hist_r = regula_falsi(f, 1.0, 2.0, toleransi)
    _, hist_fp = fixed_point(g, f, 1.5, toleransi)
    _, hist_n = newton_raphson(f, df, 1.5, toleransi)
    _, hist_s = secant(f, 1.0, 2.0, toleransi)

    plot_riwayat("Biseksi", hist_b)
    plot_riwayat("Regula Falsi", hist_r)
    plot_riwayat("Titik Tetap", hist_fp)
    plot_riwayat("Newton-Raphson", hist_n)
    plot_riwayat("Secant", hist_s)

    plt.xlabel("Iterasi")
    plt.ylabel("Residual absolut |f(x)|")
    plt.title("Perbandingan Konvergensi")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.savefig("bab2_perbandingan_konvergensi.png", dpi=150)
    plt.show()
