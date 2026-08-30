"""Bab 3 - Verifikasi solusi menggunakan NumPy."""

import numpy as np


if __name__ == "__main__":
    A = np.array(
        [
            [2.0, 1.0, -1.0],
            [-3.0, -1.0, 2.0],
            [-2.0, 1.0, 2.0],
        ]
    )

    b = np.array([8.0, -11.0, -3.0])

    x_ref = np.linalg.solve(A, b)

    residual = b - A @ x_ref
    norm_residual = np.linalg.norm(
        residual,
        ord=np.inf,
    )

    condition = np.linalg.cond(A)

    print("Solusi NumPy     :", x_ref)
    print("Residual         :", residual)
    print("Norma residual   :", norm_residual)
    print("Condition number :", condition)
