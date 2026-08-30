"""Bab 3 - Representasi matriks dan vektor dengan NumPy."""

import numpy as np


A = np.array(
    [
        [2.0, 1.0, -1.0],
        [-3.0, -1.0, 2.0],
        [-2.0, 1.0, 2.0],
    ],
    dtype=float,
)

b = np.array([8.0, -11.0, -3.0], dtype=float)


if __name__ == "__main__":
    print("Matriks A:")
    print(A)

    print("\nVektor b:")
    print(b)

    print("\nA.shape =", A.shape)
    print("A.ndim  =", A.ndim)
    print("A.dtype =", A.dtype)
