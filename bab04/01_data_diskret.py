"""Bab 4 - Representasi data diskret menggunakan NumPy."""

import numpy as np


def validasi_data(x, y):
    """Memastikan data x dan y valid untuk interpolasi/regresi."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("x dan y harus berupa array satu dimensi.")

    if len(x) == 0:
        raise ValueError("Data tidak boleh kosong.")

    if len(x) != len(y):
        raise ValueError("Jumlah elemen x dan y harus sama.")

    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("Data harus berupa bilangan berhingga.")

    if len(np.unique(x)) != len(x):
        raise ValueError("Nilai x tidak boleh duplikat.")

    return x, y


if __name__ == "__main__":
    x = np.array([0.0, 2.0, 4.0, 6.0])
    y = np.array([25.0, 29.5, 35.0, 42.5])

    x, y = validasi_data(x, y)

    print("x =", x)
    print("y =", y)
