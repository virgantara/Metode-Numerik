# Bab 07 — Persamaan Diferensial Biasa

Kode pendamping Bab 7 buku **Metode Numerik**.

## Isi folder

| File | Isi |
|---|---|
| `01_euler.py` | Implementasi metode Euler |
| `02_rk2.py` | Implementasi Runge-Kutta orde dua metode titik tengah |
| `03_rk4.py` | Implementasi Runge-Kutta orde empat klasik |
| `04_visualisasi_solusi.py` | Perbandingan Euler, RK2, RK4, dan solusi analitik |
| `05_analisis_orde.py` | Analisis galat dan estimasi orde konvergensi |
| `06_studi_kasus_franky.py` | RK4 untuk sistem ODE gerak vertikal Thousand Sunny |

## Instalasi

```bash
python -m pip install -r requirements.txt
```

## Menjalankan contoh

```bash
python 01_euler.py
python 02_rk2.py
python 03_rk4.py
python 04_visualisasi_solusi.py
python 05_analisis_orde.py
python 06_studi_kasus_franky.py
```

Kode pada folder ini dibuat untuk tujuan pembelajaran. Mahasiswa dianjurkan
membandingkan hasil numerik dengan solusi analitik ketika tersedia dan
menguji pengaruh ukuran langkah terhadap galat.
