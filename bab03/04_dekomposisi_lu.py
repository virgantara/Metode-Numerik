"""Bab 3 - Dekomposisi LU dengan partial pivoting.

Faktorisasi yang digunakan:
    P A = L U
"""

import numpy as np


def dekomposisi_lu(A, eps=1e-14):
    """Menghasilkan matriks P, L, U sehingga P @ A = L @ U."""
    A = np.array(A, dtype=float, copy=True)

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A harus berupa matriks persegi.")

    n = A.shape[0]
    U = A.copy()
    L = np.eye(n)
    P = np.eye(n)

    for k in range(n - 1):
        pivot = k + np.argmax(np.abs(U[k:, k]))

        if abs(U[pivot, k]) < eps:
            raise np.linalg.LinAlgError(
                "Matriks singular atau hampir singular."
            )

        if pivot != k:
            U[[k, pivot], :] = U[[pivot, k], :]
            P[[k, pivot], :] = P[[pivot, k], :]

            if k > 0:
                L[[k, pivot], :k] = L[[pivot, k], :k]

        for i in range(k + 1, n):
            faktor = U[i, k] / U[k, k]
            L[i, k] = faktor
            U[i, k:] -= faktor * U[k, k:]

    if abs(U[-1, -1]) < eps:
        raise np.linalg.LinAlgError("Pivot terakhir terlalu kecil.")

    return P, L, U


def substitusi_maju(L, b, eps=1e-14):
    """Menyelesaikan L y = b untuk matriks segitiga bawah."""
    L = np.asarray(L, dtype=float)
    b = np.asarray(b, dtype=float)

    n = L.shape[0]

    if L.ndim != 2 or L.shape != (n, n):
        raise ValueError("L harus matriks persegi.")

    if b.ndim != 1 or b.shape[0] != n:
        raise ValueError("Ukuran b tidak sesuai dengan L.")

    y = np.zeros(n)

    for i in range(n):
        if abs(L[i, i]) < eps:
            raise ZeroDivisionError("Diagonal L terlalu kecil.")

        jumlah = np.dot(L[i, :i], y[:i])
        y[i] = (b[i] - jumlah) / L[i, i]

    return y


def substitusi_mundur(U, y, eps=1e-14):
    """Menyelesaikan U x = y untuk matriks segitiga atas."""
    U = np.asarray(U, dtype=float)
    y = np.asarray(y, dtype=float)

    n = U.shape[0]

    if U.ndim != 2 or U.shape != (n, n):
        raise ValueError("U harus matriks persegi.")

    if y.ndim != 1 or y.shape[0] != n:
        raise ValueError("Ukuran y tidak sesuai dengan U.")

    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        if abs(U[i, i]) < eps:
            raise ZeroDivisionError("Diagonal U terlalu kecil.")

        jumlah = np.dot(U[i, i + 1:], x[i + 1:])
        x[i] = (y[i] - jumlah) / U[i, i]

    return x


def solve_lu(A, b):
    """Menyelesaikan A x = b menggunakan faktorisasi LU."""
    P, L, U = dekomposisi_lu(A)
    pb = P @ np.asarray(b, dtype=float)
    y = substitusi_maju(L, pb)
    x = substitusi_mundur(U, y)
    return x, P, L, U


if __name__ == "__main__":
    A = np.array(
        [
            [2.0, 1.0, -1.0],
            [-3.0, -1.0, 2.0],
            [-2.0, 1.0, 2.0],
        ]
    )

    b = np.array([8.0, -11.0, -3.0])

    x, P, L, U = solve_lu(A, b)

    print("P =")
    print(P)

    print("\nL =")
    print(L)

    print("\nU =")
    print(U)

    print("\nPA = LU?", np.allclose(P @ A, L @ U))
    print("Solusi   =", x)
    print("Residual =", b - A @ x)
