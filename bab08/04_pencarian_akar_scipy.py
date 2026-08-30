"""Bab 8 - Pencarian akar menggunakan scipy.optimize.root_scalar."""

from scipy.optimize import root_scalar


def f(x):
    return x**3 - x - 2.0


if __name__ == "__main__":
    hasil = root_scalar(
        f,
        bracket=[1.0, 2.0],
        method="bisect",
        xtol=1e-8,
    )

    print("Konvergen =", hasil.converged)
    print("Akar      =", hasil.root)
    print("Iterasi   =", hasil.iterations)
    print("Residual  =", abs(f(hasil.root)))
