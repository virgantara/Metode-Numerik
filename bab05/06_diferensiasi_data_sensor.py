"""Bab 5 - Diferensiasi data diskret berjarak seragam."""

import numpy as np


def diferensiasi_data_seragam(x, y):
    """Menggunakan maju di awal, pusat di interior, mundur di akhir."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("x dan y harus berupa array satu dimensi.")

    if len(x) < 2 or len(x) != len(y):
        raise ValueError("Diperlukan minimal dua pasangan data.")

    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("Data harus berupa bilangan finite.")

    delta = np.diff(x)

    if np.any(delta <= 0):
        raise ValueError("Nilai x harus meningkat secara ketat.")

    if not np.allclose(
        delta,
        delta[0],
        rtol=1e-10,
        atol=1e-12,
    ):
        raise ValueError("Data x harus berjarak seragam.")

    h = delta[0]
    turunan = np.empty_like(y)

    turunan[0] = (y[1] - y[0]) / h

    for i in range(1, len(y) - 1):
        turunan[i] = (
            y[i + 1] - y[i - 1]
        ) / (2.0 * h)

    turunan[-1] = (
        y[-1] - y[-2]
    ) / h

    return turunan


if __name__ == "__main__":
    waktu = np.array(
        [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    )

    suhu = np.array(
        [25.0, 26.1, 27.5, 29.2, 31.4, 34.0]
    )

    laju = diferensiasi_data_seragam(
        waktu,
        suhu,
    )

    print("Waktu :", waktu)
    print("Suhu  :", suhu)
    print("dT/dt :", laju)
