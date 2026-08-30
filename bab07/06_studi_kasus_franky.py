"""Bab 7 - Studi kasus Franky: gerak vertikal Thousand Sunny dengan RK4."""

import numpy as np


G = 9.8
C = 0.15


def model(t, y):
    """Model sistem: s' = v dan v' = -g - c v."""
    s, v = y

    return np.array(
        [
            v,
            -G - C * v,
        ],
        dtype=float,
    )


def rk4_sistem(f, t0, y0, tf, h):
    """RK4 klasik untuk sistem ODE vektor."""
    if tf <= t0:
        raise ValueError("tf harus lebih besar daripada t0.")

    if not np.isfinite(h) or h <= 0:
        raise ValueError("h harus positif dan finite.")

    t = float(t0)
    y = np.asarray(
        y0,
        dtype=float,
    ).copy()

    if y.ndim != 1:
        raise ValueError("y0 harus berupa vektor satu dimensi.")

    waktu = [t]
    solusi = [y.copy()]

    while t < tf:
        h_i = min(
            h,
            tf - t,
        )

        k1 = np.asarray(
            f(t, y),
            dtype=float,
        )
        k2 = np.asarray(
            f(
                t + 0.5 * h_i,
                y + 0.5 * h_i * k1,
            ),
            dtype=float,
        )
        k3 = np.asarray(
            f(
                t + 0.5 * h_i,
                y + 0.5 * h_i * k2,
            ),
            dtype=float,
        )
        k4 = np.asarray(
            f(
                t + h_i,
                y + h_i * k3,
            ),
            dtype=float,
        )

        if not all(
            k.shape == y.shape
            for k in (k1, k2, k3, k4)
        ):
            raise ValueError(
                "Dimensi keluaran f harus sama dengan dimensi y."
            )

        if not np.all(
            np.isfinite(
                np.concatenate(
                    [k1, k2, k3, k4]
                )
            )
        ):
            raise ValueError(
                "Model menghasilkan nilai tidak finite."
            )

        y = y + (h_i / 6.0) * (
            k1
            + 2.0 * k2
            + 2.0 * k3
            + k4
        )
        t = t + h_i

        waktu.append(t)
        solusi.append(y.copy())

    return (
        np.asarray(waktu),
        np.asarray(solusi),
    )


if __name__ == "__main__":
    t, y = rk4_sistem(
        model,
        t0=0.0,
        y0=[0.0, 40.0],
        tf=8.0,
        h=0.5,
    )

    posisi = y[:, 0]
    kecepatan = y[:, 1]

    for ti, si, vi in zip(
        t,
        posisi,
        kecepatan,
    ):
        print(
            "t={:.1f} s, "
            "s={:.3f} m, "
            "v={:.3f} m/s".format(
                ti,
                si,
                vi,
            )
        )
