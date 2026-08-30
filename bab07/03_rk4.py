"""Bab 7 - Runge-Kutta orde empat klasik."""

import numpy as np


def rk4(f, t0, y0, tf, h):
    """Menyelesaikan y' = f(t,y) dengan RK4 klasik."""
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
        k3 = f(
            t[i] + 0.5 * h_i,
            y[i] + 0.5 * h_i * k2,
        )
        k4 = f(
            t[i] + h_i,
            y[i] + h_i * k3,
        )

        nilai_k = np.array(
            [k1, k2, k3, k4],
            dtype=float,
        )

        if not np.all(np.isfinite(nilai_k)):
            raise ValueError(
                "Fungsi menghasilkan nilai tidak finite."
            )

        y[i + 1] = y[i] + (h_i / 6.0) * (
            k1
            + 2.0 * k2
            + 2.0 * k3
            + k4
        )

        t[i + 1] = t[i] + h_i

    return t, y


def f(t, y):
    return y


if __name__ == "__main__":
    t, y = rk4(
        f,
        t0=0.0,
        y0=1.0,
        tf=1.0,
        h=0.1,
    )

    print("t =", t)
    print("y =", y)
