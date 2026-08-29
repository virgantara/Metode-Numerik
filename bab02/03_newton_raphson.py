"""Bab 2 - Metode Newton-Raphson."""

import math


def newton_raphson(
    f,
    df,
    x0,
    toleransi=1e-8,
    maks_iterasi=100,
    ambang_turunan=1e-14,
):
    """Mencari akar menggunakan metode Newton-Raphson."""
    if toleransi <= 0:
        raise ValueError("Toleransi harus positif.")
    if not isinstance(maks_iterasi, int) or maks_iterasi <= 0:
        raise ValueError("maks_iterasi harus berupa integer positif.")
    if ambang_turunan <= 0:
        raise ValueError("ambang_turunan harus positif.")

    x = float(x0)
    riwayat = []

    for k in range(1, maks_iterasi + 1):
        fx = f(x)
        dfx = df(x)

        if not math.isfinite(fx) or not math.isfinite(dfx):
            raise ValueError(
                "Fungsi atau turunan menghasilkan nilai tidak valid."
            )

        if abs(dfx) < ambang_turunan:
            raise ZeroDivisionError("Turunan terlalu dekat dengan nol.")

        x_baru = x - fx / dfx

        if not math.isfinite(x_baru):
            raise ValueError("Iterasi menghasilkan nilai tidak valid.")

        f_baru = f(x_baru)
        residual = abs(f_baru)
        perubahan = abs(x_baru - x)

        riwayat.append(
            {
                "iterasi": k,
                "x": x_baru,
                "residual": residual,
                "perubahan": perubahan,
            }
        )

        if residual < toleransi or perubahan < toleransi:
            return x_baru, riwayat

        x = x_baru

    raise RuntimeError("Newton-Raphson belum konvergen dalam batas iterasi.")


def f(x):
    return x**3 - x - 2


def df(x):
    return 3 * x**2 - 1


if __name__ == "__main__":
    akar, riwayat = newton_raphson(
        f,
        df,
        x0=1.5,
        toleransi=1e-8,
    )

    print("Akar     :", akar)
    print("Iterasi  :", len(riwayat))
    print("Residual :", abs(f(akar)))
