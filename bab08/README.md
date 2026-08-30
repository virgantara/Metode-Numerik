# Bab 08 — Implementasi, Pengujian, dan Praktik Komputasi Numerik Modern

Kode pendamping Bab 8 buku **Metode Numerik**.

Bab ini berfungsi sebagai bab sintesis. Fokus utamanya bukan memperkenalkan
metode numerik baru, tetapi memperlihatkan bagaimana metode dari bab-bab
sebelumnya diimplementasikan, diuji, dibandingkan, dan dicatat secara
reproducible.

## Isi folder

| File | Isi |
|---|---|
| `01_program_modular.py` | Pemisahan model, algoritma, parameter, dan evaluasi |
| `02_pengukuran_waktu.py` | Pengukuran waktu eksekusi dengan `perf_counter()` |
| `03_vektorisasi_numpy.py` | Operasi array, vektorisasi, timing, dan memori NumPy |
| `04_pencarian_akar_scipy.py` | Pencarian akar dengan `scipy.optimize.root_scalar()` |
| `05_konfigurasi_eksperimen.py` | Konfigurasi dan metadata eksperimen numerik |

## Instalasi

```bash
python -m pip install -r requirements.txt
```

## Menjalankan contoh

```bash
python 01_program_modular.py
python 02_pengukuran_waktu.py
python 03_vektorisasi_numpy.py
python 04_pencarian_akar_scipy.py
python 05_konfigurasi_eksperimen.py
```

Untuk eksperimen yang akan dipublikasikan atau digunakan kembali, catat
parameter algoritma, toleransi, ukuran langkah, data, versi pustaka, serta
hasil evaluasi seperti galat, residual, jumlah iterasi, waktu, dan memori.
