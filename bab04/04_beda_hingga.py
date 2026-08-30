"""Bab 4 - Tabel beda hingga, Newton-Gregory maju dan mundur."""

import math
import numpy as np


def tabel_beda_maju(y):
    """Membangun tabel beda maju."""
    y = np.asarray(y, dtype=float)

    if y.ndim != 1 or len(y) == 0:
        raise ValueError("y harus berupa data satu dimensi yang tidak kosong.")

    n = len(y)
    tabel = np.zeros((n, n), dtype=float)
    tabel[:, 0] = y

    for j in range(1, n):
        tabel[: n - j, j] = (
            tabel[1 : n - j + 1, j - 1]
            - tabel[: n - j, j - 1]
        )

    return tabel


def _cek_jarak_seragam(x, atol=1e-12):
    x = np.asarray(x, dtype=float)

    if x.ndim != 1 or len(x) < 2:
        raise ValueError("Diperlukan minimal dua titik x.")

    selisih = np.diff(x)

    if not np.allclose(selisih, selisih[0], atol=atol, rtol=0.0):
        raise ValueError("Data x harus berjarak seragam.")

    return float(selisih[0])


def newton_gregory_maju(x, y, x_eval):
    """Interpolasi Newton-Gregory maju."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if len(x) != len(y):
        raise ValueError("Ukuran x dan y harus sama.")

    h = _cek_jarak_seragam(x)
    tabel = tabel_beda_maju(y)

    p = (x_eval - x[0]) / h
    hasil = y[0]
    produk = 1.0

    for k in range(1, len(x)):
        produk *= p - (k - 1)
        hasil += (
            produk
            / math.factorial(k)
            * tabel[0, k]
        )

    return float(hasil)


def newton_gregory_mundur(x, y, x_eval):
    """Interpolasi Newton-Gregory mundur."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if len(x) != len(y):
        raise ValueError("Ukuran x dan y harus sama.")

    h = _cek_jarak_seragam(x)
    tabel = tabel_beda_maju(y)

    p = (x_eval - x[-1]) / h
    hasil = y[-1]
    produk = 1.0
    n = len(x)

    for k in range(1, n):
        # Δ^k y_{n-k} setara dengan ∇^k y_n
        beda_mundur = tabel[n - k - 1, k]
        produk *= p + (k - 1)
        hasil += (
            produk
            / math.factorial(k)
            * beda_mundur
        )

    return float(hasil)


if __name__ == "__main__":
    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    y = np.array([1.0, 2.0, 5.0, 10.0, 17.0])

    print("Tabel beda maju:")
    print(tabel_beda_maju(y))

    print("\nP_maju(0.5)  =", newton_gregory_maju(x, y, 0.5))
    print("P_mundur(3.5) =", newton_gregory_mundur(x, y, 3.5))
