"""Bab 8 - Pemisahan model, algoritma, parameter, dan evaluasi."""

import math


def fungsi_model(x):
    """Model matematika yang akan dicari akarnya."""
    return x**3 - x - 2.0


def biseksi(
    f,
    a,
    b,
    toleransi=1e-8,
    maks_iterasi=100,
):
    """Mencari akar dengan metode Biseksi."""
    if toleransi <= 0:
        raise ValueError("Toleransi harus positif.")

    if not isinstance(maks_iterasi, int) or maks_iterasi <= 0:
        raise ValueError("maks_iterasi harus berupa integer positif.")

    fa = f(a)
    fb = f(b)

    if not math.isfinite(fa) or not math.isfinite(fb):
        raise ValueError("Nilai fungsi awal harus finite.")

    if fa == 0:
        return a, 0

    if fb == 0:
        return b, 0

    if fa * fb > 0:
        raise ValueError(
            "Interval awal tidak memiliki perubahan tanda."
        )

    for k in range(1, maks_iterasi + 1):
        c = 0.5 * (a + b)
        fc = f(c)

        if not math.isfinite(fc):
            raise ValueError(
                "Fungsi menghasilkan nilai tidak finite."
            )

        if abs(fc) < toleransi:
            return c, k

        if 0.5 * abs(b - a) < toleransi:
            return c, k

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    raise RuntimeError(
        "Batas iterasi tercapai sebelum konvergen."
    )


def residual(f, x):
    """Menghitung residual absolut."""
    return abs(f(x))


if __name__ == "__main__":
    akar, iterasi = biseksi(
        fungsi_model,
        1.0,
        2.0,
        toleransi=1e-8,
    )

    print("Akar     =", akar)
    print("Iterasi  =", iterasi)
    print("Residual =", residual(fungsi_model, akar))
