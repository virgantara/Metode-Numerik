"""Bab 4 - Visualisasi regresi linear dan regresi polinomial."""

import numpy as np
import matplotlib.pyplot as plt


def regresi_linear(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    x_rata = np.mean(x)
    y_rata = np.mean(y)

    a1 = np.sum(
        (x - x_rata) * (y - y_rata)
    ) / np.sum((x - x_rata) ** 2)

    a0 = y_rata - a1 * x_rata

    return a0, a1


def regresi_polinomial(x, y, derajat):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    X = np.vander(
        x,
        N=derajat + 1,
        increasing=True,
    )

    koefisien, _, _, _ = np.linalg.lstsq(
        X,
        y,
        rcond=None,
    )

    return koefisien


if __name__ == "__main__":
    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    y = np.array([1.0, 2.0, 2.0, 4.0, 5.0])

    a0, a1 = regresi_linear(x, y)
    coef2 = regresi_polinomial(x, y, derajat=2)

    x_plot = np.linspace(
        x.min(),
        x.max(),
        200,
    )

    y_linear = a0 + a1 * x_plot
    y_polinomial = sum(
        coef2[i] * x_plot**i
        for i in range(len(coef2))
    )

    plt.scatter(x, y, label="Data")
    plt.plot(
        x_plot,
        y_linear,
        label="Regresi Linear",
    )
    plt.plot(
        x_plot,
        y_polinomial,
        label="Regresi Polinomial",
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Aproksimasi Data dengan Least Squares")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("bab4_regresi_least_squares.png", dpi=150)
    plt.show()
