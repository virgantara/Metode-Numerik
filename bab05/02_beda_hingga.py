"""Bab 5 - Beda maju, beda mundur, dan beda pusat."""

import numpy as np


def _validasi_h(h):
    if not np.isfinite(h) or h <= 0:
        raise ValueError("h harus berupa bilangan finite dan positif.")


def _validasi_nilai(*nilai):
    if not all(np.isfinite(v) for v in nilai):
        raise ValueError("Fungsi menghasilkan nilai tidak finite.")


def beda_maju(f, x, h):
    """Aproksimasi turunan pertama dengan beda maju."""
    _validasi_h(h)

    fx = f(x)
    fxh = f(x + h)
    _validasi_nilai(fx, fxh)

    return (fxh - fx) / h


def beda_mundur(f, x, h):
    """Aproksimasi turunan pertama dengan beda mundur."""
    _validasi_h(h)

    fx = f(x)
    fxh = f(x - h)
    _validasi_nilai(fx, fxh)

    return (fx - fxh) / h


def beda_pusat(f, x, h):
    """Aproksimasi turunan pertama dengan beda pusat."""
    _validasi_h(h)

    fplus = f(x + h)
    fminus = f(x - h)
    _validasi_nilai(fplus, fminus)

    return (fplus - fminus) / (2.0 * h)


if __name__ == "__main__":
    f = np.sin
    df = np.cos

    x = 1.0
    h = 0.1
    eksak = df(x)

    maju = beda_maju(f, x, h)
    mundur = beda_mundur(f, x, h)
    pusat = beda_pusat(f, x, h)

    print("Turunan analitik :", eksak)
    print("Beda maju        :", maju)
    print("Beda mundur      :", mundur)
    print("Beda pusat       :", pusat)

    print("\nGalat maju   :", abs(maju - eksak))
    print("Galat mundur :", abs(mundur - eksak))
    print("Galat pusat  :", abs(pusat - eksak))
