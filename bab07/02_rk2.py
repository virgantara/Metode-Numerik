"""Bab 7 - Runge-Kutta orde dua metode titik tengah."""

import numpy as np


def rk2(f, t0, y0, tf, h):
    """Menyelesaikan y' = f(t,y) dengan RK2 titik tengah."""
    if tf <= t0:
        raise ValueError("tf harus lebih besar daripada t0.")

    if not np.isfinite(h) or h <= 0:
        raise ValueError("h harus positif dan finite.")

    n = int(np.ceil((tf - t0) / h))

    t = np.empty(n + 1, dtype=float)
    y = np.empty(n + 1, dtype=float)

    t[0] = t0
    y[0] = y0

    for i in range(n):
        h_i = min(h, tf - t[i])

        k1 = f(t[i], y[i])
        k2 = f(
            t[i] + 0.5 * h_i,
            y[i] + 0.5 * h_i * k1,
        )

        if not np.isfinite(k1) or not np.isfinite(k2):
            raise ValueError(
                "Fungsi menghasilkan nilai tidak finite."
            )

        y[i + 1] = y[i] + h_i * k2
        t[i + 1] = t[i] + h_i

    return t, y


def f(t, y):
    return y


if __name__ == "__main__":
    t, y = rk2(
        f,
        t0=0.0,
        y0=1.0,
        tf=1.0,
        h=0.1,
    )

    print("t =", t)
    print("y =", y)
