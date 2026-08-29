"""Bab 1 - Iterasi Babylonian sederhana untuk menghampiri akar dua."""

import math


def main():
    x = 1.0
    maks_iterasi = 10

    for k in range(maks_iterasi):
        if x == 0:
            raise ZeroDivisionError("Nilai iterasi tidak boleh nol.")

        x_baru = 0.5 * (x + 2.0 / x)
        galat = abs(math.sqrt(2.0) - x_baru)

        print(
            f"iterasi={k + 1:2d}, "
            f"x={x_baru:.12f}, "
            f"galat={galat:.3e}"
        )

        x = x_baru


if __name__ == "__main__":
    main()
