"""Bab 5 - Grafik log-log ukuran langkah terhadap galat."""

import numpy as np
import matplotlib.pyplot as plt


def beda_maju(f, x, h):
    return (f(x + h) - f(x)) / h


def beda_mundur(f, x, h):
    return (f(x) - f(x - h)) / h


def beda_pusat(f, x, h):
    return (f(x + h) - f(x - h)) / (2.0 * h)


if __name__ == "__main__":
    f = np.sin
    df = np.cos

    x = 1.0
    eksak = df(x)

    h_values = np.logspace(-1, -14, 100)

    error_maju = np.array(
        [abs(beda_maju(f, x, h) - eksak) for h in h_values]
    )

    error_mundur = np.array(
        [abs(beda_mundur(f, x, h) - eksak) for h in h_values]
    )

    error_pusat = np.array(
        [abs(beda_pusat(f, x, h) - eksak) for h in h_values]
    )

    plt.loglog(
        h_values,
        error_maju,
        label="Beda maju",
    )
    plt.loglog(
        h_values,
        error_mundur,
        label="Beda mundur",
    )
    plt.loglog(
        h_values,
        error_pusat,
        label="Beda pusat",
    )

    plt.xlabel("Ukuran langkah h")
    plt.ylabel("Galat absolut")
    plt.title("Pengaruh Ukuran Langkah terhadap Galat")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        "bab5_loglog.png",
        dpi=150,
    )

    plt.show()
