"""Bab 4 - Interpolasi Lagrange."""

import numpy as np


def lagrange_interpolasi(x_data, y_data, x_eval):
    """Menghitung interpolasi Lagrange pada satu atau banyak titik."""
    x_data = np.asarray(x_data, dtype=float)
    y_data = np.asarray(y_data, dtype=float)

    if x_data.ndim != 1 or y_data.ndim != 1:
        raise ValueError("x_data dan y_data harus satu dimensi.")

    if len(x_data) == 0 or len(x_data) != len(y_data):
        raise ValueError("Data kosong atau ukuran x dan y tidak sama.")

    if len(np.unique(x_data)) != len(x_data):
        raise ValueError("Nilai x_data tidak boleh duplikat.")

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

    if np.ndim(x_eval) == 0:
        return float(hasil)

    return hasil


if __name__ == "__main__":
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([2.0, 3.0, 5.0])

    x_eval = 2.5
    hasil = lagrange_interpolasi(x, y, x_eval)

    print("x evaluasi =", x_eval)
    print("Interpolasi =", hasil)
