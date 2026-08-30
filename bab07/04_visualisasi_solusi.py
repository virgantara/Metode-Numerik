"""Bab 7 - Visualisasi Euler, RK2, RK4, dan solusi analitik."""

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


def f(t, y):
    return y - t**2 + 1.0


def solusi_eksak(t):
    return (t + 1.0) ** 2 - 0.5 * np.exp(t)


if __name__ == "__main__":
    t_e, y_e = euler(
        f,
        0.0,
        0.5,
        2.0,
        0.2,
    )

    t_2, y_2 = rk2(
        f,
        0.0,
        0.5,
        2.0,
        0.2,
    )

    t_4, y_4 = rk4(
        f,
        0.0,
        0.5,
        2.0,
        0.2,
    )

    t_ref = np.linspace(
        0.0,
        2.0,
        500,
    )

    plt.plot(
        t_ref,
        solusi_eksak(t_ref),
        label="Analitik",
    )
    plt.plot(
        t_e,
        y_e,
        marker="o",
        label="Euler",
    )
    plt.plot(
        t_2,
        y_2,
        marker="s",
        label="RK2",
    )
    plt.plot(
        t_4,
        y_4,
        marker="^",
        label="RK4",
    )

    plt.xlabel("Waktu t")
    plt.ylabel("y(t)")
    plt.title("Perbandingan Solusi ODE")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(
        "bab7_perbandingan_solusi.png",
        dpi=150,
    )
    plt.show()
