"""Bab 6 - Aturan Trapesium komposit untuk fungsi analitik."""

import numpy as np


def trapesium(f, a, b, n):
    """Mengaproksimasi integral f pada [a,b] dengan n subinterval."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n harus berupa integer positif.")
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
    integral = h * (
        0.5 * y[0]
        + np.sum(y[1:-1])
        + 0.5 * y[-1]
    )
    return float(integral)


def f(x):
    return x**2


if __name__ == "__main__":
    hasil = trapesium(f, 0.0, 2.0, 4)
    print("Integral Trapesium =", hasil)
