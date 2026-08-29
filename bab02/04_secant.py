"""Bab 2 - Metode Secant."""

import math


def secant(f, x0, x1, toleransi=1e-8, maks_iterasi=100):
    """Mencari akar menggunakan metode Secant."""
    if toleransi <= 0:
        raise ValueError("Toleransi harus positif.")
    if not isinstance(maks_iterasi, int) or maks_iterasi <= 0:
        raise ValueError("maks_iterasi harus berupa integer positif.")

    x0 = float(x0)
    x1 = float(x1)
    f0 = f(x0)
    f1 = f(x1)

    if not math.isfinite(f0) or not math.isfinite(f1):
        raise ValueError("Nilai fungsi awal tidak valid.")

    riwayat = []

    for k in range(1, maks_iterasi + 1):
        pembagi = f1 - f0

        if abs(pembagi) <= math.ulp(1.0):
            raise ZeroDivisionError("Selisih nilai fungsi terlalu kecil.")

        x2 = x1 - f1 * (x1 - x0) / pembagi

        if not math.isfinite(x2):
            raise ValueError("Iterasi menghasilkan nilai tidak valid.")

        f2 = f(x2)

        if not math.isfinite(f2):
            raise ValueError("Fungsi menghasilkan nilai tidak valid.")

        residual = abs(f2)
        perubahan = abs(x2 - x1)

        riwayat.append(
            {
                "iterasi": k,
                "x_sebelumnya": x0,
                "x_saat_ini": x1,
                "x": x2,
                "residual": residual,
                "perubahan": perubahan,
            }
        )

        if residual < toleransi or perubahan < toleransi:
            return x2, riwayat

        x0, x1 = x1, x2
        f0, f1 = f1, f2

    raise RuntimeError("Metode Secant belum konvergen dalam batas iterasi.")


def f(x):
    return x**3 - x - 2


if __name__ == "__main__":
    akar, riwayat = secant(
        f,
        x0=1.0,
        x1=2.0,
        toleransi=1e-8,
    )

    print("Akar     :", akar)
    print("Iterasi  :", len(riwayat))
    print("Residual :", abs(f(akar)))
