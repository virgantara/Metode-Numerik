"""Bab 3 - Metode Gauss-Jordan dengan partial pivoting."""

import numpy as np


def gauss_jordan(A, b, eps=1e-14):
    """Menyelesaikan A x = b dengan reduksi Gauss-Jordan."""
    A = np.array(A, dtype=float, copy=True)
    b = np.array(b, dtype=float, copy=True)

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A harus berupa matriks persegi.")

    n = A.shape[0]

    if b.ndim != 1 or b.shape[0] != n:
        raise ValueError("Ukuran b tidak sesuai dengan A.")

    augmented = np.column_stack((A, b))

    for k in range(n):
        pivot = k + np.argmax(np.abs(augmented[k:, k]))

        if abs(augmented[pivot, k]) < eps:
            raise np.linalg.LinAlgError(
                "Matriks singular atau hampir singular."
            )

        if pivot != k:
            augmented[[k, pivot]] = augmented[[pivot, k]]

        # Normalisasi baris pivot
        augmented[k] /= augmented[k, k]

        # Nolkan semua elemen lain pada kolom pivot
        for i in range(n):
            if i == k:
                continue

            faktor = augmented[i, k]
            augmented[i] -= faktor * augmented[k]

    x = augmented[:, -1]
    return x, augmented


if __name__ == "__main__":
    A = np.array(
        [
            [2.0, 1.0, -1.0],
            [-3.0, -1.0, 2.0],
            [-2.0, 1.0, 2.0],
        ]
    )

    b = np.array([8.0, -11.0, -3.0])

    x, hasil = gauss_jordan(A, b)

    print("Bentuk [I|x]:")
    print(hasil)

    print("\nSolusi   =", x)
    print("Residual =", b - A @ x)
