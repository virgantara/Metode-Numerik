"""Bab 7 - Metode Euler untuk PDB/ODE skalar."""

import numpy as np


def _validasi_interval(t0, tf, h):
    if not np.isfinite(t0) or not np.isfinite(tf):
        raise ValueError("t0 dan tf harus berupa bilangan finite.")

    if tf <= t0:
        raise ValueError("tf harus lebih besar daripada t0.")

    if not np.isfinite(h) or h <= 0:
        raise ValueError("h harus berupa bilangan finite dan positif.")


def euler(f, t0, y0, tf, h):
    """Menyelesaikan y' = f(t,y) dengan metode Euler."""
    _validasi_interval(t0, tf, h)

    n = int(np.ceil((tf - t0) / h))

    t = np.empty(n + 1, dtype=float)
    y = np.empty(n + 1, dtype=float)

    t[0] = t0
    y[0] = y0

    for i in range(n):
        h_i = min(h, tf - t[i])
        nilai_f = f(t[i], y[i])

        if not np.isfinite(nilai_f):
            raise ValueError(
                "Fungsi menghasilkan nilai tidak finite."
            )

        y[i + 1] = y[i] + h_i * nilai_f
        t[i + 1] = t[i] + h_i

    return t, y


def f(t, y):
    return y


if __name__ == "__main__":
    t, y = euler(
        f,
        t0=0.0,
        y0=1.0,
        tf=1.0,
        h=0.1,
    )

    print("t =", t)
    print("y =", y)
