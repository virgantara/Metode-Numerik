# Bab 02 — Penyelesaian Akar Persamaan Nonlinear

Kode pendamping Bab 2 buku **Metode Numerik**.

## Isi folder

| File | Isi |
|---|---|
| `01_biseksi_regula_falsi.py` | Implementasi Biseksi dan Regula Falsi |
| `02_fixed_point.py` | Implementasi Iterasi Titik Tetap |
| `03_newton_raphson.py` | Implementasi Newton-Raphson |
| `04_secant.py` | Implementasi metode Secant |
| `05_visualisasi_konvergensi.py` | Perbandingan residual terhadap iterasi |

## Instalasi

```bash
python -m pip install -r requirements.txt
```

## Menjalankan contoh

```bash
python 01_biseksi_regula_falsi.py
python 02_fixed_point.py
python 03_newton_raphson.py
python 04_secant.py
python 05_visualisasi_konvergensi.py
```

Seluruh contoh utama menggunakan fungsi

\[
f(x)=x^3-x-2.
\]

Kode dibuat untuk keperluan pembelajaran. Riwayat iterasi dikembalikan agar
mahasiswa dapat memeriksa residual, perubahan antaritasi, dan pola konvergensi.
