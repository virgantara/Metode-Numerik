"""Bab 1 - Akumulasi galat floating-point pada penjumlahan berulang."""

import math
import numpy as np


def main():
    n = 100_000
    nilai = 0.1

    akumulasi = 0.0
    for _ in range(n):
        akumulasi += nilai

    teoritis = n * nilai
    galat = abs(teoritis - akumulasi)
    fsum = math.fsum([nilai] * n)
    numpy_sum = np.sum(np.full(n, nilai, dtype=np.float64))

    print("Hasil akumulasi biasa =", akumulasi)
    print("Nilai teoritis        =", teoritis)
    print("Galat absolut         =", galat)
    print("Dengan math.fsum      =", fsum)
    print("Dengan numpy.sum      =", numpy_sum)


if __name__ == "__main__":
    main()
