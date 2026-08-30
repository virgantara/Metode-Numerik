"""Bab 4 - Visualisasi data dan kurva interpolasi Lagrange."""

import numpy as np
import matplotlib.pyplot as plt


def lagrange_interpolasi(x_data, y_data, x_eval):
    x_data = np.asarray(x_data, dtype=float)
    y_data = np.asarray(y_data, dtype=float)
    x_eval_arr = np.asarray(x_eval, dtype=float)

    hasil = np.zeros_like(x_eval_arr, dtype=float)
    n = len(x_data)

    for i in range(n):
        basis = np.ones_like(x_eval_arr, dtype=float)

        for j in range(n):
            if i != j:
                basis *= (
                    (x_eval_arr - x_data[j])
                    / (x_data[i] - x_data[j])
                )

        hasil += y_data[i] * basis

    return hasil


if __name__ == "__main__":
    x = np.array([0.0, 2.0, 4.0, 6.0])
    y = np.array([25.0, 29.5, 35.0, 42.5])

    x_plot = np.linspace(
        x.min(),
        x.max(),
        200,
    )

    y_plot = lagrange_interpolasi(
        x,
        y,
        x_plot,
    )

    plt.scatter(x, y, label="Data")
    plt.plot(
        x_plot,
        y_plot,
        label="Interpolasi Lagrange",
    )

    plt.xlabel("Waktu (menit)")
    plt.ylabel("Suhu (derajat C)")
    plt.title("Interpolasi Data Suhu")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("bab4_interpolasi_suhu.png", dpi=150)
    plt.show()
