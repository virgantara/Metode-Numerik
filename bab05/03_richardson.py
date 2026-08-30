"""Bab 5 - Ekstrapolasi Richardson untuk beda pusat."""

import numpy as np


def beda_pusat(f, x, h):
    if not np.isfinite(h) or h <= 0:
        raise ValueError("h harus berupa bilangan finite dan positif.")

    fplus = f(x + h)
    fminus = f(x - h)

    if not np.isfinite(fplus) or not np.isfinite(fminus):
        raise ValueError("Fungsi menghasilkan nilai tidak finite.")

    return (fplus - fminus) / (2.0 * h)


def richardson_pusat(f, x, h):
    """Meningkatkan beda pusat orde dua menjadi aproksimasi orde empat."""
    d_h = beda_pusat(f, x, h)
    d_h2 = beda_pusat(f, x, h / 2.0)

    return (4.0 * d_h2 - d_h) / 3.0


if __name__ == "__main__":
    f = np.sin
    df = np.cos

    x = 1.0
    h = 0.2

    d_h = beda_pusat(f, x, h)
    d_h2 = beda_pusat(f, x, h / 2.0)
    hasil = richardson_pusat(f, x, h)
    eksak = df(x)

    print("Beda pusat h     :", d_h)
    print("Beda pusat h/2   :", d_h2)
    print("Richardson       :", hasil)
    print("Analitik         :", eksak)
    print("Galat Richardson :", abs(hasil - eksak))
