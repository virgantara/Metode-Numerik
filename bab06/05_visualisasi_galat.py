"""Bab 6 - Visualisasi galat Trapesium dan Simpson."""

import numpy as np
import matplotlib.pyplot as plt


def trapesium(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = np.asarray(f(x), dtype=float)
    h = (b - a) / n
    return float(
        h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
    )


def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson 1/3 komposit memerlukan n genap.")
    x = np.linspace(a, b, n + 1)
    y = np.asarray(f(x), dtype=float)
    h = (b - a) / n
    return float(
        (h / 3.0) * (
            y[0]
            + y[-1]
            + 4.0 * np.sum(y[1:-1:2])
            + 2.0 * np.sum(y[2:-1:2])
        )
    )


if __name__ == "__main__":
    f = np.sin
    nilai_eksak = 2.0
    n_values = np.array([2, 4, 8, 16, 32, 64, 128])

    error_trap = []
    error_simp = []

    for n in n_values:
        n = int(n)
        t = trapesium(f, 0.0, np.pi, n)
        s = simpson(f, 0.0, np.pi, n)

        error_trap.append(abs(t - nilai_eksak))
        error_simp.append(abs(s - nilai_eksak))

    plt.loglog(n_values, error_trap, marker="o", label="Trapesium")
    plt.loglog(n_values, error_simp, marker="s", label="Simpson")

    plt.xlabel("Jumlah subinterval n")
    plt.ylabel("Galat absolut")
    plt.title("Konvergensi Integrasi Numerik")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.savefig("bab6_konvergensi_integrasi.png", dpi=150)
    plt.show()
