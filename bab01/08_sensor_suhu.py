"""Bab 1 - Eksplorasi awal model kalibrasi sensor suhu."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

V_UKUR = 1.2


def tegangan(T):
    return 0.002 * T**2 + 0.01 * T + 0.5


def residual(T):
    return tegangan(T) - V_UKUR


def main():
    T = np.linspace(0.0, 30.0, 301)
    r = residual(T)

    if not np.all(np.isfinite(r)):
        raise ValueError("Ditemukan nilai residual tidak valid.")

    indeks = np.argmin(np.abs(r))
    T_terdekat = T[indeks]

    print("Suhu kandidat =", T_terdekat)
    print("Residual =", residual(T_terdekat))

    plt.plot(T, r)
    plt.axhline(0.0)
    plt.xlabel("Suhu T (°C)")
    plt.ylabel("Residual f(T)")
    plt.title("Residual Model Kalibrasi Sensor")
    plt.grid(True)
    plt.tight_layout()

    output = Path(__file__).with_name("bab01_residual_sensor.png")
    plt.savefig(output, dpi=160)
    print("Grafik disimpan di:", output)
    plt.show()


if __name__ == "__main__":
    main()
