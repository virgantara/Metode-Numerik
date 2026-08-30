"""Bab 6 - Aturan Simpson 1/3 komposit."""

import numpy as np


def simpson(f, a, b, n):
    """Mengaproksimasi integral f pada [a,b] dengan Simpson 1/3 komposit."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n harus berupa integer positif.")
    if n % 2 != 0:
        raise ValueError("Aturan Simpson 1/3 komposit memerlukan n genap.")
    if not np.isfinite(a) or not np.isfinite(b):
        raise ValueError("Batas integral harus finite.")
    if a == b:
        return 0.0

    x = np.linspace(a, b, n + 1)
    y = np.asarray(f(x), dtype=float)

    if y.shape != x.shape:
        raise ValueError("Fungsi harus menghasilkan nilai untuk setiap titik x.")
    if not np.all(np.isfinite(y)):
        raise ValueError("Fungsi menghasilkan nilai tidak finite.")

    h = (b - a) / n
    jumlah_ganjil = np.sum(y[1:-1:2])
    jumlah_genap = np.sum(y[2:-1:2])

    integral = (h / 3.0) * (
        y[0]
        + y[-1]
        + 4.0 * jumlah_ganjil
        + 2.0 * jumlah_genap
    )
    return float(integral)


def f(x):
    return x**2


if __name__ == "__main__":
    hasil = simpson(f, 0.0, 2.0, 4)
    print("Integral Simpson =", hasil)
