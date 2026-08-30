"""Bab 6 - Aturan Trapesium untuk data diskret tidak seragam."""

import numpy as np


def trapesium_data(x, y):
    """Mengintegralkan pasangan data (x,y) dengan interval boleh tidak seragam."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("x dan y harus berupa array satu dimensi.")
    if len(x) < 2 or len(x) != len(y):
        raise ValueError("Diperlukan minimal dua pasangan data.")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("Data harus berupa bilangan finite.")

    dx = np.diff(x)
    if np.any(dx <= 0):
        raise ValueError("Nilai x harus meningkat secara ketat.")

    luas = 0.5 * dx * (y[:-1] + y[1:])
    return float(np.sum(luas))


if __name__ == "__main__":
    # waktu dalam sekon, daya dalam watt
    waktu = np.array([0.0, 1.0, 2.5, 4.0])
    daya = np.array([10.0, 12.0, 17.0, 20.0])

    energi = trapesium_data(waktu, daya)
    print("Energi aproksimasi =", energi, "joule")
