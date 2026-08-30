"""Bab 6 - Verifikasi integral menggunakan SciPy."""

import numpy as np
from scipy.integrate import quad


def f(x):
    return np.exp(-x**2)


if __name__ == "__main__":
    a = 0.0
    b = 1.0

    hasil, estimasi_error = quad(f, a, b)

    print("Hasil SciPy    =", hasil)
    print("Estimasi error =", estimasi_error)
