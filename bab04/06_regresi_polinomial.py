"""Bab 4 - Regresi polinomial menggunakan least squares."""

import numpy as np


def regresi_polinomial(x, y, derajat):
    """Menghasilkan koefisien polinom, RMSE, prediksi, dan residual."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("x dan y harus satu dimensi.")

    if len(x) == 0 or len(x) != len(y):
        raise ValueError("Data kosong atau ukuran x dan y tidak sama.")

    if not isinstance(derajat, int) or derajat < 0:
        raise ValueError("Derajat harus berupa integer nonnegatif.")

    if derajat >= len(x):
        raise ValueError(
            "Derajat polinom harus lebih kecil daripada jumlah data."
        )

    X = np.vander(
        x,
        N=derajat + 1,
        increasing=True,
    )

    koefisien, _, rank, _ = np.linalg.lstsq(
        X,
        y,
        rcond=None,
    )

    if rank < derajat + 1:
        raise np.linalg.LinAlgError(
            "Matriks desain tidak memiliki rank penuh."
        )

    y_pred = X @ koefisien
    residual = y - y_pred
    rmse = np.sqrt(np.mean(residual**2))

    return koefisien, rmse, y_pred, residual


def evaluasi_polinomial(koefisien, x):
    """Mengevaluasi a0 + a1*x + ... + am*x^m."""
    koefisien = np.asarray(koefisien, dtype=float)
    x = np.asarray(x, dtype=float)

    hasil = np.zeros_like(x, dtype=float)

    for i, a in enumerate(koefisien):
        hasil += a * x**i

    if np.ndim(x) == 0:
        return float(hasil)

    return hasil


if __name__ == "__main__":
    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    y = np.array([1.0, 2.0, 2.0, 4.0, 5.0])

    koefisien, rmse, _, _ = regresi_polinomial(
        x,
        y,
        derajat=2,
    )

    print("Koefisien =", koefisien)
    print("RMSE      =", rmse)
