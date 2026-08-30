"""Bab 5 - Studi kasus Chopper: pemantauan laju perubahan suhu.

Ambang pada contoh ini bersifat ilustratif untuk pembelajaran,
bukan kriteria diagnosis medis.
"""

import numpy as np


def laju_beda_mundur(waktu, suhu):
    waktu = np.asarray(waktu, dtype=float)
    suhu = np.asarray(suhu, dtype=float)

    if waktu.ndim != 1 or suhu.ndim != 1:
        raise ValueError("waktu dan suhu harus satu dimensi.")

    if len(waktu) < 2 or len(waktu) != len(suhu):
        raise ValueError("Data tidak cukup atau ukuran data tidak sama.")

    if not np.all(np.diff(waktu) > 0):
        raise ValueError("Waktu harus meningkat secara ketat.")

    laju = np.full_like(
        suhu,
        np.nan,
        dtype=float,
    )

    for i in range(1, len(suhu)):
        h = waktu[i] - waktu[i - 1]
        laju[i] = (
            suhu[i] - suhu[i - 1]
        ) / h

    return laju


if __name__ == "__main__":
    waktu = np.array(
        [0, 10, 20, 30, 40],
        dtype=float,
    )

    suhu = np.array(
        [38.1, 38.4, 38.9, 39.0, 38.8],
        dtype=float,
    )

    ambang = 0.04
    laju = laju_beda_mundur(waktu, suhu)

    for i in range(1, len(suhu)):
        status = (
            "PERHATIAN"
            if laju[i] > ambang
            else "Normal"
        )

        print(
            "t={:.0f} menit, T={:.1f} C, "
            "dT/dt={:.3f} C/menit, {}".format(
                waktu[i],
                suhu[i],
                laju[i],
                status,
            )
        )
