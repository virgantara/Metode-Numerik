"""Bab 4 - Interpolasi Newton dengan beda terbagi."""

import numpy as np


def koefisien_newton(x, y):
    """Menghitung koefisien beda terbagi Newton."""
    x = np.asarray(x, dtype=float)
    coef = np.asarray(y, dtype=float).copy()

    if x.ndim != 1 or coef.ndim != 1:
        raise ValueError("x dan y harus satu dimensi.")

    if len(x) == 0 or len(x) != len(coef):
        raise ValueError("Data kosong atau ukuran x dan y tidak sama.")

    if len(np.unique(x)) != len(x):
        raise ValueError("Nilai x tidak boleh duplikat.")

    n = len(x)

    for j in range(1, n):
        penyebut = x[j:n] - x[0:n-j]

        if np.any(np.isclose(penyebut, 0.0)):
            raise ZeroDivisionError("Terdapat penyebut beda terbagi nol.")

        coef[j:n] = (
            coef[j:n] - coef[j-1:n-1]
        ) / penyebut

    return coef


def evaluasi_newton(x_data, coef, x_eval):
    """Mengevaluasi polinom Newton menggunakan bentuk bersarang."""
    x_data = np.asarray(x_data, dtype=float)
    coef = np.asarray(coef, dtype=float)

    if len(x_data) != len(coef):
        raise ValueError("Ukuran x_data dan koefisien harus sama.")

    x_eval_arr = np.asarray(x_eval, dtype=float)

    hasil = np.full_like(
        x_eval_arr,
        coef[-1],
        dtype=float,
    )

    for k in range(len(coef) - 2, -1, -1):
        hasil = coef[k] + (x_eval_arr - x_data[k]) * hasil

    if np.ndim(x_eval) == 0:
        return float(hasil)

    return hasil


if __name__ == "__main__":
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([2.0, 3.0, 5.0])

    coef = koefisien_newton(x, y)
    hasil = evaluasi_newton(x, coef, 2.5)

    print("Koefisien Newton =", coef)
    print("P(2.5) =", hasil)
