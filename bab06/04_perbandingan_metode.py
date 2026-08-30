"""Bab 6 - Perbandingan Trapesium dan Simpson terhadap nilai analitik."""

import numpy as np


def trapesium(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = np.asarray(f(x), dtype=float)
    h = (b - a) / n
    return float(
        h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
    )


def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson 1/3 komposit memerlukan n genap.")
    x = np.linspace(a, b, n + 1)
    y = np.asarray(f(x), dtype=float)
    h = (b - a) / n
    return float(
        (h / 3.0) * (
            y[0]
            + y[-1]
            + 4.0 * np.sum(y[1:-1:2])
            + 2.0 * np.sum(y[2:-1:2])
        )
    )


if __name__ == "__main__":
    f = np.sin
    a = 0.0
    b = np.pi
    nilai_eksak = 2.0

    print(
        f"{'n':>4} {'Trapesium':>14} {'Error T':>12} "
        f"{'Simpson':>14} {'Error S':>12}"
    )

    for n in [2, 4, 8, 16, 32, 64]:
        trap = trapesium(f, a, b, n)
        simp = simpson(f, a, b, n)

        error_trap = abs(nilai_eksak - trap)
        error_simp = abs(nilai_eksak - simp)

        print(
            f"{n:4d} {trap:14.10f} {error_trap:12.3e} "
            f"{simp:14.10f} {error_simp:12.3e}"
        )
