# Bab 03 — Sistem Persamaan Linear

Kode pendamping Bab 3 buku **Metode Numerik**.

## Isi folder

| File | Isi |
|---|---|
| `01_representasi_matriks.py` | Representasi matriks dan vektor dengan NumPy |
| `02_eliminasi_gauss.py` | Eliminasi Gauss dengan partial pivoting |
| `03_gauss_jordan.py` | Metode Gauss-Jordan |
| `04_dekomposisi_lu.py` | Dekomposisi LU dengan partial pivoting |
| `05_jacobi.py` | Metode iterasi Jacobi |
| `06_gauss_seidel.py` | Metode Gauss-Seidel |
| `07_visualisasi_konvergensi.py` | Grafik residual Jacobi dan Gauss-Seidel |
| `08_verifikasi_numpy.py` | Verifikasi dengan `numpy.linalg.solve()` dan condition number |

## Instalasi

```bash
python -m pip install -r requirements.txt
```

## Menjalankan contoh

```bash
python 01_representasi_matriks.py
python 02_eliminasi_gauss.py
python 03_gauss_jordan.py
python 04_dekomposisi_lu.py
python 05_jacobi.py
python 06_gauss_seidel.py
python 07_visualisasi_konvergensi.py
python 08_verifikasi_numpy.py
```

Implementasi pada folder ini ditujukan untuk pembelajaran. Untuk aplikasi
numerik nyata, pustaka numerik yang matang seperti NumPy/SciPy umumnya lebih
tepat digunakan.
