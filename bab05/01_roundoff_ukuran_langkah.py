"""Bab 5 - Pengaruh ukuran langkah sangat kecil pada diferensiasi numerik."""

import numpy as np


def beda_maju(f, x, h):
    if h <= 0:
        raise ValueError("h harus positif.")

    fx = f(x)
    fxh = f(x + h)

    if not np.isfinite(fx) or not np.isfinite(fxh):
        raise ValueError("Fungsi menghasilkan nilai tidak finite.")

    return (fxh - fx) / h


if __name__ == "__main__":
    x = 1.0
    nilai_eksak = np.cos(x)

    h_values = [
        1e-2,
        1e-4,
        1e-6,
        1e-8,
        1e-10,
        1e-12,
        1e-14,
    ]

    print(f"{'h':>12} {'aproksimasi':>18} {'galat':>18}")

    for h in h_values:
        aproksimasi = beda_maju(np.sin, x, h)
        galat = abs(aproksimasi - nilai_eksak)

        print(
            f"{h:12.1e} "
            f"{aproksimasi:18.12e} "
            f"{galat:18.12e}"
        )
