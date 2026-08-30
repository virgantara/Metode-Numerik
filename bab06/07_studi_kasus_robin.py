"""Bab 6 - Studi kasus Robin: estimasi luas teluk dari data diskret."""

import numpy as np


def trapesium_data_seragam(y, h):
    y = np.asarray(y, dtype=float)

    if y.ndim != 1 or len(y) < 2:
        raise ValueError("Diperlukan minimal dua data y.")
    if h <= 0:
        raise ValueError("h harus positif.")

    return float(
        h * (
            0.5 * y[0]
            + np.sum(y[1:-1])
            + 0.5 * y[-1]
        )
    )


def simpson_data_seragam(y, h):
    y = np.asarray(y, dtype=float)
    n = len(y) - 1

    if n <= 0:
        raise ValueError("Data tidak cukup.")
    if n % 2 != 0:
        raise ValueError(
            "Jumlah subinterval harus genap untuk Simpson 1/3."
        )
    if h <= 0:
        raise ValueError("h harus positif.")

    return float(
        (h / 3.0) * (
            y[0]
            + y[-1]
            + 4.0 * np.sum(y[1:-1:2])
            + 2.0 * np.sum(y[2:-1:2])
        )
    )


if __name__ == "__main__":
    jarak = np.array(
        [0, 50, 100, 150, 200, 250, 300, 350, 400],
        dtype=float,
    )
    lebar = np.array(
        [0, 32, 48, 55, 60, 52, 40, 25, 0],
        dtype=float,
    )

    delta = np.diff(jarak)

    if not np.allclose(delta, delta[0]):
        raise ValueError("Data harus berjarak seragam untuk contoh ini.")

    h = float(delta[0])

    luas_trapesium = trapesium_data_seragam(lebar, h)
    luas_simpson = simpson_data_seragam(lebar, h)

    print("Luas Trapesium =", luas_trapesium, "m^2")
    print("Luas Simpson   =", luas_simpson, "m^2")
