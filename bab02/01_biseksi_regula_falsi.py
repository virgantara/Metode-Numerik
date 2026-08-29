"""Bab 2 - Metode Biseksi dan Regula Falsi.

Contoh pendamping buku Metode Numerik.
"""

import math


def _validasi_umum(toleransi, maks_iterasi):
    if toleransi <= 0:
        raise ValueError("Toleransi harus positif.")
    if not isinstance(maks_iterasi, int) or maks_iterasi <= 0:
        raise ValueError("maks_iterasi harus berupa integer positif.")


def biseksi(f, a, b, toleransi=1e-8, maks_iterasi=100):
    """Mencari akar dengan metode Biseksi."""
    _validasi_umum(toleransi, maks_iterasi)

    fa = f(a)
    fb = f(b)

    if not math.isfinite(fa) or not math.isfinite(fb):
        raise ValueError("Nilai fungsi pada interval awal tidak valid.")

    if fa == 0:
        return a, []
    if fb == 0:
        return b, []

    if fa * fb > 0:
        raise ValueError("Interval awal tidak memiliki perubahan tanda.")

    riwayat = []

    for k in range(1, maks_iterasi + 1):
        c = 0.5 * (a + b)
        fc = f(c)

        if not math.isfinite(fc):
            raise ValueError("Fungsi menghasilkan nilai tidak valid.")

        riwayat.append(
            {
                "iterasi": k,
                "a": a,
                "b": b,
                "x": c,
                "residual": abs(fc),
                "lebar_interval": abs(b - a),
            }
        )

        if abs(fc) < toleransi or 0.5 * abs(b - a) < toleransi:
            return c, riwayat

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    raise RuntimeError("Biseksi belum konvergen dalam batas iterasi.")


def regula_falsi(f, a, b, toleransi=1e-8, maks_iterasi=100):
    """Mencari akar dengan metode Regula Falsi klasik."""
    _validasi_umum(toleransi, maks_iterasi)

    fa = f(a)
    fb = f(b)

    if not math.isfinite(fa) or not math.isfinite(fb):
        raise ValueError("Nilai fungsi pada interval awal tidak valid.")

    if fa == 0:
        return a, []
    if fb == 0:
        return b, []

    if fa * fb > 0:
        raise ValueError("Interval awal tidak memiliki perubahan tanda.")

    riwayat = []
    x_sebelumnya = None

    for k in range(1, maks_iterasi + 1):
        pembagi = fb - fa

        if abs(pembagi) <= math.ulp(1.0):
            raise ZeroDivisionError("Selisih nilai fungsi terlalu kecil.")

        x = b - fb * (b - a) / pembagi
        fx = f(x)

        if not math.isfinite(x) or not math.isfinite(fx):
            raise ValueError("Iterasi menghasilkan nilai tidak valid.")

        perubahan = None if x_sebelumnya is None else abs(x - x_sebelumnya)

        riwayat.append(
            {
                "iterasi": k,
                "a": a,
                "b": b,
                "x": x,
                "residual": abs(fx),
                "perubahan": perubahan,
            }
        )

        if abs(fx) < toleransi:
            return x, riwayat

        if perubahan is not None and perubahan < toleransi:
            return x, riwayat

        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        x_sebelumnya = x

    raise RuntimeError("Regula Falsi belum konvergen dalam batas iterasi.")


def f(x):
    return x**3 - x - 2


if __name__ == "__main__":
    akar_b, hist_b = biseksi(f, 1.0, 2.0)
    akar_r, hist_r = regula_falsi(f, 1.0, 2.0)

    print("Biseksi")
    print("  Akar     :", akar_b)
    print("  Iterasi  :", len(hist_b))
    print("  Residual :", abs(f(akar_b)))

    print("\nRegula Falsi")
    print("  Akar     :", akar_r)
    print("  Iterasi  :", len(hist_r))
    print("  Residual :", abs(f(akar_r)))
