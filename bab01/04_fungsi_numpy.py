"""Bab 1 - Evaluasi fungsi pada beberapa titik menggunakan NumPy."""

import numpy as np


def f(x):
    return x**3 - x - 2


def main():
    x = np.linspace(0.0, 2.0, 5)
    y = f(x)

    print("x =", x)
    print("y =", y)


if __name__ == "__main__":
    main()
