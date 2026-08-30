"""Bab 3 - Metode Iterasi Jacobi."""

import numpy as np


def jacobi(A, b, x0=None, toleransi=1e-8, maks_iterasi=1000):
    """Menyelesaikan A x = b menggunakan metode Jacobi."""
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A harus berupa matriks persegi.")

    n = A.shape[0]

    if b.ndim != 1 or b.shape[0] != n:
        raise ValueError("Ukuran b tidak sesuai dengan A.")

    if toleransi <= 0:
        raise ValueError("Toleransi harus positif.")

    if not isinstance(maks_iterasi, int) or maks_iterasi <= 0:
        raise ValueError("maks_iterasi harus berupa integer positif.")

    diagonal = np.diag(A)

    if np.any(np.abs(diagonal) < 1e-14):
        raise ZeroDivisionError(
            "Terdapat elemen diagonal terlalu kecil."
        )

    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float, copy=True)

        if x.shape != (n,):
            raise ValueError("Ukuran x0 tidak sesuai.")

    R = A - np.diagflat(diagonal)
    riwayat = []

    for k in range(1, maks_iterasi + 1):
        x_baru = (b - R @ x) / diagonal

        perubahan = np.linalg.norm(
            x_baru - x,
            ord=np.inf,
        )

        residual = np.linalg.norm(
            b - A @ x_baru,
            ord=np.inf,
        )

        riwayat.append(
            {
                "iterasi": k,
                "x": x_baru.copy(),
                "perubahan": perubahan,
                "residual": residual,
            }
        )

        if perubahan < toleransi or residual < toleransi:
            return x_baru, riwayat

        x = x_baru

    raise RuntimeError(
        "Jacobi belum konvergen dalam batas iterasi."
    )


if __name__ == "__main__":
    A = np.array(
        [
            [10.0, -1.0, 2.0],
            [-1.0, 11.0, -1.0],
            [2.0, -1.0, 10.0],
        ]
    )

    b = np.array([6.0, 25.0, -11.0])

    solusi, riwayat = jacobi(
        A,
        b,
        x0=np.zeros(3),
        toleransi=1e-8,
    )

    print("Solusi   =", solusi)
    print("Iterasi  =", len(riwayat))
    print("Residual =", riwayat[-1]["residual"])
