"""Bab 1 - Penghentian iterasi berdasarkan toleransi."""

import math


def akar_dua(toleransi=1e-8, maks_iterasi=100):
    if toleransi <= 0:
        raise ValueError("Toleransi harus bernilai positif.")

    if not isinstance(maks_iterasi, int) or maks_iterasi <= 0:
        raise ValueError("maks_iterasi harus berupa integer positif.")

    x = 1.0

    for k in range(1, maks_iterasi + 1):
        if x == 0:
            raise ZeroDivisionError("Pembagian dengan nol pada iterasi.")

        x_baru = 0.5 * (x + 2.0 / x)
        perubahan = abs(x_baru - x)

        if perubahan < toleransi:
            return x_baru, k, perubahan

        x = x_baru

    raise RuntimeError("Metode belum konvergen dalam batas iterasi.")


def main():
    hasil, iterasi, perubahan = akar_dua(
        toleransi=1e-10,
        maks_iterasi=100,
    )

    print("Hasil =", hasil)
    print("Iterasi =", iterasi)
    print("Perubahan =", perubahan)
    print("Referensi =", math.sqrt(2.0))


if __name__ == "__main__":
    main()
