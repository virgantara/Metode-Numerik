"""Bab 3 - Visualisasi konvergensi Jacobi dan Gauss-Seidel."""

import numpy as np
import matplotlib.pyplot as plt


def jacobi(A, b, x0=None, toleransi=1e-8, maks_iterasi=1000):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)

    n = A.shape[0]
    diagonal = np.diag(A)

    if np.any(np.abs(diagonal) < 1e-14):
        raise ZeroDivisionError("Diagonal terlalu kecil.")

    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float, copy=True)
    R = A - np.diagflat(diagonal)
    riwayat = []

    for k in range(1, maks_iterasi + 1):
        x_baru = (b - R @ x) / diagonal
        perubahan = np.linalg.norm(x_baru - x, ord=np.inf)
        residual = np.linalg.norm(b - A @ x_baru, ord=np.inf)

        riwayat.append(
            {
                "iterasi": k,
                "residual": residual,
                "perubahan": perubahan,
            }
        )

        if perubahan < toleransi or residual < toleransi:
            return x_baru, riwayat

        x = x_baru

    raise RuntimeError("Jacobi belum konvergen.")


def gauss_seidel(A, b, x0=None, toleransi=1e-8, maks_iterasi=1000):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)

    n = A.shape[0]
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float, copy=True)
    riwayat = []

    for k in range(1, maks_iterasi + 1):
        x_lama = x.copy()

        for i in range(n):
            jumlah_kiri = np.dot(A[i, :i], x[:i])
            jumlah_kanan = np.dot(A[i, i + 1:], x_lama[i + 1:])
            x[i] = (b[i] - jumlah_kiri - jumlah_kanan) / A[i, i]

        perubahan = np.linalg.norm(x - x_lama, ord=np.inf)
        residual = np.linalg.norm(b - A @ x, ord=np.inf)

        riwayat.append(
            {
                "iterasi": k,
                "residual": residual,
                "perubahan": perubahan,
            }
        )

        if perubahan < toleransi or residual < toleransi:
            return x.copy(), riwayat

    raise RuntimeError("Gauss-Seidel belum konvergen.")


def ambil_residual(riwayat):
    return [item["residual"] for item in riwayat]


if __name__ == "__main__":
    A = np.array(
        [
            [10.0, -1.0, 2.0],
            [-1.0, 11.0, -1.0],
            [2.0, -1.0, 10.0],
        ]
    )

    b = np.array([6.0, 25.0, -11.0])
    x0 = np.zeros(3)

    _, hist_jacobi = jacobi(A, b, x0=x0)
    _, hist_gs = gauss_seidel(A, b, x0=x0)

    r_jacobi = ambil_residual(hist_jacobi)
    r_gs = ambil_residual(hist_gs)

    plt.semilogy(
        range(1, len(r_jacobi) + 1),
        r_jacobi,
        marker="o",
        label="Jacobi",
    )

    plt.semilogy(
        range(1, len(r_gs) + 1),
        r_gs,
        marker="s",
        label="Gauss-Seidel",
    )

    plt.xlabel("Iterasi")
    plt.ylabel("Norma residual")
    plt.title("Konvergensi Sistem Persamaan Linear")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.savefig("bab3_konvergensi_jacobi_gauss_seidel.png", dpi=150)
    plt.show()
