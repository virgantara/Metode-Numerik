"""Bab 3 - Eliminasi Gauss dengan partial pivoting."""

import numpy as np


def _validasi_sistem(A, b):
    A = np.array(A, dtype=float, copy=True)
    b = np.array(b, dtype=float, copy=True)

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A harus berupa matriks persegi.")

    if b.ndim != 1 or b.shape[0] != A.shape[0]:
        raise ValueError("Ukuran b tidak sesuai dengan A.")

    return A, b


def eliminasi_gauss(A, b, eps=1e-14):
    """Menyelesaikan A x = b menggunakan Eliminasi Gauss dan partial pivoting."""
    A, b = _validasi_sistem(A, b)

    if eps <= 0:
        raise ValueError("eps harus positif.")

    n = A.shape[0]

    # Eliminasi maju
    for k in range(n - 1):
        pivot = k + np.argmax(np.abs(A[k:, k]))

        if abs(A[pivot, k]) < eps:
            raise np.linalg.LinAlgError(
                "Matriks singular atau hampir singular."
            )

        if pivot != k:
            A[[k, pivot]] = A[[pivot, k]]
            b[[k, pivot]] = b[[pivot, k]]

        for i in range(k + 1, n):
            faktor = A[i, k] / A[k, k]
            A[i, k:] -= faktor * A[k, k:]
            b[i] -= faktor * b[k]

    if abs(A[-1, -1]) < eps:
        raise np.linalg.LinAlgError("Pivot terakhir terlalu kecil.")

    # Substitusi mundur
    x = np.zeros(n, dtype=float)

    for i in range(n - 1, -1, -1):
        if abs(A[i, i]) < eps:
            raise np.linalg.LinAlgError(
                "Elemen diagonal terlalu kecil."
            )

        jumlah = np.dot(A[i, i + 1:], x[i + 1:])
        x[i] = (b[i] - jumlah) / A[i, i]

    return x


if __name__ == "__main__":
    A = np.array(
        [
            [2.0, 1.0, -1.0],
            [-3.0, -1.0, 2.0],
            [-2.0, 1.0, 2.0],
        ]
    )

    b = np.array([8.0, -11.0, -3.0])

    x = eliminasi_gauss(A, b)

    print("Solusi   =", x)
    print("Residual =", b - A @ x)
