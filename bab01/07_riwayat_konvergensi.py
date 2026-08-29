"""Bab 1 - Pencatatan dan visualisasi galat iterasi akar dua."""

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def proses_iterasi(toleransi=1e-12, maks_iterasi=50):
    if toleransi <= 0:
        raise ValueError("Toleransi harus positif.")

    if not isinstance(maks_iterasi, int) or maks_iterasi <= 0:
        raise ValueError("maks_iterasi harus berupa integer positif.")

    x = 1.0
    riwayat = []

    for k in range(1, maks_iterasi + 1):
        if abs(x) < np.finfo(float).eps:
            raise ZeroDivisionError("Nilai x terlalu dekat dengan nol.")

        x_baru = 0.5 * (x + 2.0 / x)
        galat_abs = abs(math.sqrt(2.0) - x_baru)
        perubahan = abs(x_baru - x)

        riwayat.append((k, x_baru, galat_abs, perubahan))

        if perubahan < toleransi:
            break

        x = x_baru

    return riwayat


def main():
    data = proses_iterasi()

    iterasi = [baris[0] for baris in data]
    galat = [baris[2] for baris in data]

    plt.semilogy(iterasi, galat, marker="o")
    plt.xlabel("Iterasi")
    plt.ylabel("Galat absolut")
    plt.title("Konvergensi Aproksimasi Akar Dua")
    plt.grid(True)
    plt.tight_layout()

    output = Path(__file__).with_name("bab01_konvergensi_akar_dua.png")
    plt.savefig(output, dpi=160)
    print("Grafik disimpan di:", output)
    plt.show()


if __name__ == "__main__":
    main()
