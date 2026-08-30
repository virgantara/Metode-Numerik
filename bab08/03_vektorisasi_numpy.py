"""Bab 8 - Operasi berbasis array dan vektorisasi NumPy."""

from time import perf_counter

import numpy as np


def berbasis_array(x):
    """Menghitung fungsi pada seluruh array sekaligus."""
    return np.sin(x) + 0.5 * x**2


def berbasis_loop(x):
    """Versi loop Python sebagai pembanding sederhana."""
    hasil = np.empty_like(x)

    for i, nilai in enumerate(x):
        hasil[i] = np.sin(nilai) + 0.5 * nilai**2

    return hasil


if __name__ == "__main__":
    x = np.linspace(
        0.0,
        10.0,
        100_000,
    )

    awal = perf_counter()
    y_array = berbasis_array(x)
    waktu_array = perf_counter() - awal

    awal = perf_counter()
    y_loop = berbasis_loop(x)
    waktu_loop = perf_counter() - awal

    print(
        "Hasil sama?",
        np.allclose(y_array, y_loop),
    )
    print("Waktu array =", waktu_array)
    print("Waktu loop  =", waktu_loop)
    print("Memori x    =", x.nbytes, "byte")
    print("Memori y    =", y_array.nbytes, "byte")
