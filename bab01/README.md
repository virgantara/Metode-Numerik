# Bab 01 — Dasar-Dasar Metode Numerik, Galat, dan Konvergensi

Kode pendamping Bab 1 buku **Metode Numerik**.

## Daftar program

| File | Materi |
|---|---|
| `01_floating_point.py` | Keterbatasan representasi floating-point dan `np.isclose()` |
| `02_akumulasi_floating_point.py` | Akumulasi galat dan perbandingan `float`, `math.fsum()`, serta `numpy.sum()` |
| `03_fungsi_matematika.py` | Representasi fungsi matematika dengan Python |
| `04_fungsi_numpy.py` | Evaluasi fungsi pada array NumPy |
| `05_iterasi_akar_dua.py` | Iterasi Babylonian untuk menghampiri √2 |
| `06_toleransi_akar_dua.py` | Kriteria penghentian berbasis toleransi |
| `07_riwayat_konvergensi.py` | Pencatatan riwayat dan grafik konvergensi |
| `08_sensor_suhu.py` | Eksplorasi residual model kalibrasi sensor suhu |

## Instalasi

```bash
pip install -r requirements.txt
```

## Menjalankan program

Contoh:

```bash
python 01_floating_point.py
python 07_riwayat_konvergensi.py
python 08_sensor_suhu.py
```

Program visualisasi akan menyimpan gambar PNG pada folder yang sama dan juga menampilkan grafik.

## Catatan

Kode pada repositori dibuat sedikit lebih lengkap daripada potongan kode yang sebelumnya dicetak di buku: indentasi dibenahi, validasi input dibuat konsisten, dan program visualisasi menyimpan grafik agar eksperimen lebih mudah direproduksi.
