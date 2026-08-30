"""Bab 8 - Pengukuran waktu eksekusi algoritma numerik."""

from math import sin
from time import perf_counter


def algoritma(jumlah_titik=200_000):
    """Contoh beban numerik sederhana untuk demonstrasi timing."""
    if not isinstance(jumlah_titik, int) or jumlah_titik <= 0:
        raise ValueError(
            "jumlah_titik harus berupa integer positif."
        )

    total = 0.0

    for i in range(jumlah_titik):
        x = i / jumlah_titik
        total += sin(x)

    return total / jumlah_titik


def ukur_waktu(fungsi, *args, pengulangan=5):
    """Menjalankan fungsi beberapa kali dan mengembalikan waktu setiap run."""
    if pengulangan <= 0:
        raise ValueError("pengulangan harus positif.")

    waktu = []
    hasil = None

    for _ in range(pengulangan):
        awal = perf_counter()
        hasil = fungsi(*args)
        akhir = perf_counter()

        waktu.append(akhir - awal)

    return hasil, waktu


if __name__ == "__main__":
    hasil, waktu = ukur_waktu(
        algoritma,
        200_000,
        pengulangan=5,
    )

    print("Hasil              =", hasil)
    print("Waktu tiap run (s) =", waktu)
    print(
        "Waktu minimum (s)  =",
        min(waktu),
    )
    print(
        "Waktu rata-rata (s)=",
        sum(waktu) / len(waktu),
    )
