"""Bab 7 - Pengujian galat terhadap ukuran langkah."""

import numpy as np
import matplotlib.pyplot as plt


def euler(f, t0, y0, tf, h):
    n = int(np.ceil((tf - t0) / h))
    t = np.empty(n + 1)
    y = np.empty(n + 1)
    t[0], y[0] = t0, y0

    for i in range(n):
        h_i = min(h, tf - t[i])
        y[i + 1] = y[i] + h_i * f(t[i], y[i])
        t[i + 1] = t[i] + h_i

    return t, y


def rk2(f, t0, y0, tf, h):
    n = int(np.ceil((tf - t0) / h))
    t = np.empty(n + 1)
    y = np.empty(n + 1)
    t[0], y[0] = t0, y0

    for i in range(n):
        h_i = min(h, tf - t[i])
        k1 = f(t[i], y[i])
        k2 = f(
            t[i] + 0.5 * h_i,
            y[i] + 0.5 * h_i * k1,
        )
        y[i + 1] = y[i] + h_i * k2
        t[i + 1] = t[i] + h_i

    return t, y


def rk4(f, t0, y0, tf, h):
    n = int(np.ceil((tf - t0) / h))
    t = np.empty(n + 1)
    y = np.empty(n + 1)
    t[0], y[0] = t0, y0

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

        y[i + 1] = y[i] + (h_i / 6.0) * (
            k1 + 2.0 * k2 + 2.0 * k3 + k4
        )
        t[i + 1] = t[i] + h_i

    return t, y


def estimasi_orde(error):
    """Estimasi orde dari rasio galat ketika h dibagi dua."""
    error = np.asarray(error, dtype=float)

    return np.log2(
        error[:-1] / error[1:]
    )


def f(t, y):
    return y


def exact(t):
    return np.exp(t)


if __name__ == "__main__":
    h_values = np.array(
        [0.2, 0.1, 0.05, 0.025]
    )

    error_euler = []
    error_rk2 = []
    error_rk4 = []

    ref = exact(1.0)

    for h in h_values:
        _, y1 = euler(
            f,
            0.0,
            1.0,
            1.0,
            float(h),
        )
        _, y2 = rk2(
            f,
            0.0,
            1.0,
            1.0,
            float(h),
        )
        _, y4 = rk4(
            f,
            0.0,
            1.0,
            1.0,
            float(h),
        )

        error_euler.append(abs(y1[-1] - ref))
        error_rk2.append(abs(y2[-1] - ref))
        error_rk4.append(abs(y4[-1] - ref))

    print("h =", h_values)
    print("Galat Euler =", error_euler)
    print("Galat RK2   =", error_rk2)
    print("Galat RK4   =", error_rk4)

    print("\nEstimasi orde Euler =", estimasi_orde(error_euler))
    print("Estimasi orde RK2   =", estimasi_orde(error_rk2))
    print("Estimasi orde RK4   =", estimasi_orde(error_rk4))

    plt.loglog(
        h_values,
        error_euler,
        marker="o",
        label="Euler",
    )
    plt.loglog(
        h_values,
        error_rk2,
        marker="s",
        label="RK2",
    )
    plt.loglog(
        h_values,
        error_rk4,
        marker="^",
        label="RK4",
    )

    plt.xlabel("Ukuran langkah h")
    plt.ylabel("Galat pada t=1")
    plt.title("Analisis Orde Metode ODE")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.savefig(
        "bab7_analisis_orde.png",
        dpi=150,
    )
    plt.show()
