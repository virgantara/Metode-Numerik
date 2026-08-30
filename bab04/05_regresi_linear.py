"""Bab 4 - Regresi linear dengan metode kuadrat terkecil."""

import numpy as np


def regresi_linear(x, y):
    """Menghasilkan a0, a1, RMSE, prediksi, dan residual."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("x dan y harus satu dimensi.")

    if len(x) < 2 or len(x) != len(y):
        raise ValueError("Diperlukan minimal dua pasangan data.")

    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("Data harus berupa bilangan berhingga.")

    x_rata = np.mean(x)
    y_rata = np.mean(y)

    penyebut = np.sum((x - x_rata) ** 2)

    if np.isclose(penyebut, 0.0):
        raise ValueError("Semua nilai x sama; regresi linear tidak dapat dihitung.")

    a1 = np.sum(
        (x - x_rata) * (y - y_rata)
    ) / penyebut

    a0 = y_rata - a1 * x_rata

    y_pred = a0 + a1 * x
    residual = y - y_pred
    rmse = np.sqrt(np.mean(residual**2))

    return a0, a1, rmse, y_pred, residual


if __name__ == "__main__":
    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    y = np.array([1.0, 2.0, 2.0, 4.0, 5.0])

    a0, a1, rmse, y_pred, residual = regresi_linear(x, y)

    print("a0       =", a0)
    print("a1       =", a1)
    print("Prediksi =", y_pred)
    print("Residual =", residual)
    print("RMSE     =", rmse)
