"""Bab 5 - Eksperimen beberapa ukuran langkah h."""

import numpy as np


def beda_maju(f, x, h):
    return (f(x + h) - f(x)) / h


def beda_mundur(f, x, h):
    return (f(x) - f(x - h)) / h


def beda_pusat(f, x, h):
    return (f(x + h) - f(x - h)) / (2.0 * h)


def richardson_pusat(f, x, h):
    d_h = beda_pusat(f, x, h)
    d_h2 = beda_pusat(f, x, h / 2.0)

    return (4.0 * d_h2 - d_h) / 3.0


if __name__ == "__main__":
    f = np.sin
    df = np.cos

    x = 1.0
    eksak = df(x)

    h_values = 10.0 ** (-np.arange(1, 15))

    header = (
        f"{'h':>11} "
        f"{'E maju':>13} "
        f"{'E mundur':>13} "
        f"{'E pusat':>13} "
        f"{'E Richardson':>15}"
    )
    print(header)

    for h in h_values:
        e_maju = abs(beda_maju(f, x, h) - eksak)
        e_mundur = abs(beda_mundur(f, x, h) - eksak)
        e_pusat = abs(beda_pusat(f, x, h) - eksak)
        e_richardson = abs(richardson_pusat(f, x, h) - eksak)

        print(
            f"{h:11.1e} "
            f"{e_maju:13.5e} "
            f"{e_mundur:13.5e} "
            f"{e_pusat:13.5e} "
            f"{e_richardson:15.5e}"
        )
