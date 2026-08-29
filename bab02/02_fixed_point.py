"""Bab 2 - Iterasi Titik Tetap."""

import math
import numpy as np


def fixed_point(g, f, x0, toleransi=1e-8, maks_iterasi=100):
    """Mencari titik tetap x = g(x) sekaligus memeriksa residual f(x)."""
    if toleransi <= 0:
        raise ValueError("Toleransi harus positif.")
    if not isinstance(maks_iterasi, int) or maks_iterasi <= 0:
        raise ValueError("maks_iterasi harus berupa integer positif.")

    x = float(x0)
    riwayat = []

    for k in range(1, maks_iterasi + 1):
        x_baru = g(x)

        if not math.isfinite(x_baru):
            raise ValueError("Fungsi iterasi menghasilkan nilai tidak valid.")

        fx = f(x_baru)

        if not math.isfinite(fx):
            raise ValueError("Fungsi menghasilkan nilai tidak valid.")

        residual = abs(fx)
        perubahan = abs(x_baru - x)

        riwayat.append(
            {
                "iterasi": k,
                "x": x_baru,
                "residual": residual,
                "perubahan": perubahan,
            }
        )

        if residual < toleransi or perubahan < toleransi:
            return x_baru, riwayat

        x = x_baru

    raise RuntimeError(
        "Iterasi Titik Tetap belum konvergen dalam batas iterasi."
    )


def f(x):
    return x**3 - x - 2


def g(x):
    return np.cbrt(x + 2)


if __name__ == "__main__":
    akar, riwayat = fixed_point(
        g,
        f,
        x0=1.5,
        toleransi=1e-8,
    )

    print("Akar     :", akar)
    print("Iterasi  :", len(riwayat))
    print("Residual :", abs(f(akar)))
