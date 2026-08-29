"""Bab 1 - Keterbatasan representasi floating-point."""

import numpy as np


def main():
    a = 0.1
    b = 0.2
    c = 0.3

    hasil = a + b

    print("a + b =", hasil)
    print("c =", c)
    print("Sama persis?", hasil == c)
    print("Hampir sama?", np.isclose(hasil, c))
    print("Selisih =", hasil - c)


if __name__ == "__main__":
    main()
