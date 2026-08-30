# Metode Numerik

Repositori pendamping buku **Metode Numerik: Konsep, Algoritma, dan Penerapan untuk Komputasi Modern**.

Repositori ini berisi implementasi Python, eksperimen numerik, visualisasi, dan contoh program yang melengkapi pembahasan pada buku. Materi utama seperti konsep, formulasi matematika, algoritma, contoh perhitungan, analisis galat, dan interpretasi hasil tetap dibahas di dalam buku, sedangkan kode lengkap ditempatkan di repositori ini agar lebih mudah dijalankan, dimodifikasi, dan dikembangkan.

## Tentang Buku

Buku ini membahas konsep dasar metode numerik dengan pendekatan yang menggabungkan:

- formulasi matematika;
- algoritma dan pseudocode;
- contoh perhitungan;
- implementasi Python;
- visualisasi;
- analisis galat dan konvergensi;
- studi kasus komputasi.

Repositori ini ditujukan terutama sebagai **companion code** bagi pembaca buku, mahasiswa, dosen, dan siapa pun yang ingin mempelajari metode numerik melalui eksperimen langsung menggunakan Python.

## Struktur Repositori

```text
Metode-Numerik/
├── README.md
├── requirements.txt
│
├── bab01/
│   ├── README.md
│   └── *.py
│
├── bab02/
│   ├── README.md
│   └── *.py
│
├── bab03/
│   ├── README.md
│   └── *.py
│
├── bab04/
│   ├── README.md
│   └── *.py
│
├── bab05/
│   ├── README.md
│   └── *.py
│
├── bab06/
│   ├── README.md
│   └── *.py
│
├── bab07/
│   ├── README.md
│   └── *.py
│
└── bab08/
    ├── README.md
    └── *.py
```

Setiap folder bab memiliki `README.md` sendiri yang menjelaskan isi program dan cara menjalankannya.

## Daftar Bab

| Folder | Bab | Pokok Bahasan |
|---|---|---|
| `bab01/` | Dasar-Dasar Metode Numerik, Galat, dan Konvergensi | floating-point, galat, toleransi, iterasi, konvergensi |
| `bab02/` | Penyelesaian Akar Persamaan Nonlinear | Biseksi, Regula Falsi, Fixed-Point, Newton-Raphson, Secant |
| `bab03/` | Sistem Persamaan Linear | Eliminasi Gauss, Gauss-Jordan, Dekomposisi LU, Jacobi, Gauss-Seidel |
| `bab04/` | Interpolasi dan Aproksimasi Data | Lagrange, Newton, beda hingga, least squares, regresi linear dan polinomial |
| `bab05/` | Diferensiasi Numerik | beda maju, beda mundur, beda pusat, Richardson, analisis galat |
| `bab06/` | Integrasi Numerik | Trapesium, Simpson, integrasi data diskret, analisis galat |
| `bab07/` | Persamaan Diferensial Biasa | Euler, RK2, RK4, sistem ODE, analisis orde |
| `bab08/` | Implementasi, Pengujian, dan Praktik Komputasi Numerik Modern | modularisasi, benchmarking, NumPy, SciPy, reproducibility |

## Persyaratan

Kode dikembangkan menggunakan Python 3 dan beberapa pustaka komputasi ilmiah.

Pustaka utama yang digunakan:

```text
numpy
matplotlib
scipy
```

Disarankan menggunakan **Python 3.10 atau lebih baru**.

## Instalasi

Clone repositori:

```bash
git clone https://github.com/virgantara/Metode-Numerik.git
cd Metode-Numerik
```

Opsional tetapi disarankan: buat virtual environment.

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Kemudian instal dependensi:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Jika suatu folder bab memiliki `requirements.txt` tersendiri, dependensi juga dapat dipasang langsung dari folder tersebut.

Contoh:

```bash
cd bab06
pip install -r requirements.txt
```

## Menjalankan Program

Setiap file Python dapat dijalankan secara langsung.

Contoh:

```bash
python bab02/03_newton_raphson.py
```

atau:

```bash
cd bab07
python 03_rk4.py
```

Beberapa program menghasilkan grafik menggunakan Matplotlib. Grafik akan ditampilkan ketika program dijalankan dan, pada beberapa contoh, juga disimpan sebagai file gambar.

## Contoh Penggunaan

### Akar Persamaan Nonlinear

```bash
python bab02/01_biseksi_regula_falsi.py
python bab02/03_newton_raphson.py
python bab02/04_secant.py
```

### Sistem Persamaan Linear

```bash
python bab03/02_eliminasi_gauss.py
python bab03/04_dekomposisi_lu.py
python bab03/05_jacobi.py
python bab03/06_gauss_seidel.py
```

### Interpolasi dan Regresi

```bash
python bab04/02_lagrange_interpolasi.py
python bab04/03_newton_interpolasi.py
python bab04/05_regresi_linear.py
python bab04/06_regresi_polinomial.py
```

### Diferensiasi Numerik

```bash
python bab05/02_beda_hingga.py
python bab05/03_richardson.py
python bab05/05_visualisasi_galat.py
```

### Integrasi Numerik

```bash
python bab06/01_trapesium_komposit.py
python bab06/03_simpson_komposit.py
python bab06/05_visualisasi_galat.py
```

### Persamaan Diferensial Biasa

```bash
python bab07/01_euler.py
python bab07/02_rk2.py
python bab07/03_rk4.py
python bab07/05_analisis_orde.py
```

## Filosofi Repositori

Repositori ini tidak dimaksudkan untuk menggantikan pembahasan di dalam buku.

Pembagian materinya adalah:

> **Buku** = konsep + matematika + algoritma + contoh hitung + analisis  
> **GitHub** = kode lengkap + eksperimen + visualisasi + pengujian

Dengan pendekatan ini, pembaca dapat memahami alasan matematis suatu metode dari buku, kemudian menjalankan dan memodifikasi implementasinya di komputer.

## Verifikasi Hasil

Pada banyak contoh, implementasi manual dibandingkan dengan pustaka numerik seperti NumPy atau SciPy.

Tujuannya bukan hanya mendapatkan jawaban numerik, tetapi juga memeriksa:

- residual;
- galat absolut dan relatif;
- jumlah iterasi;
- orde konvergensi;
- sensitivitas terhadap parameter;
- pengaruh ukuran langkah;
- waktu komputasi.

Untuk penggunaan nyata, pustaka numerik yang matang dan teruji biasanya lebih disarankan daripada implementasi pembelajaran yang ditulis dari awal.

## Reproduksibilitas

Agar eksperimen dapat direproduksi, sebaiknya catat:

- versi Python;
- versi NumPy, SciPy, dan Matplotlib;
- data masukan;
- nilai awal;
- toleransi;
- ukuran langkah;
- jumlah iterasi maksimum;
- metode yang digunakan;
- hasil numerik dan residual.

Versi pustaka dapat diperiksa dengan:

```bash
python --version
pip freeze
```

## Catatan untuk Pembaca Buku

Nama folder dan file di repositori dibuat agar konsisten dengan referensi kode pada buku.

Jika buku menampilkan:

```text
bab03/04_dekomposisi_lu.py
```

maka file tersebut dapat ditemukan pada:

```text
https://github.com/virgantara/Metode-Numerik/blob/main/bab03/04_dekomposisi_lu.py
```

Untuk melihat seluruh kode pada suatu bab, buka folder bab yang bersangkutan.

Contoh:

```text
https://github.com/virgantara/Metode-Numerik/tree/main/bab04
```

## Pengembangan dan Eksperimen

Pembaca dipersilakan menggunakan kode sebagai dasar untuk eksperimen, misalnya:

- mengubah nilai awal;
- mengubah toleransi;
- mengubah ukuran langkah;
- menggunakan fungsi lain;
- membandingkan beberapa metode;
- menambahkan pengukuran waktu;
- menambahkan data sendiri;
- membuat grafik konvergensi;
- membandingkan implementasi dengan NumPy atau SciPy.

## Kontribusi

Jika menemukan kesalahan kode, ketidaksesuaian hasil, atau ingin mengusulkan perbaikan, silakan membuat **Issue** atau **Pull Request** pada repositori ini.

Saat melaporkan masalah, sebaiknya sertakan:

1. nama bab dan file;
2. versi Python;
3. input yang digunakan;
4. output yang diperoleh;
5. output yang diharapkan;
6. pesan error, jika ada.

## Sitasi

Jika repositori atau buku ini digunakan dalam karya ilmiah, tugas akhir, materi pembelajaran, atau publikasi, silakan mencantumkan sitasi terhadap buku sesuai informasi bibliografi pada edisi yang digunakan.

Informasi sitasi yang lebih lengkap dapat ditambahkan setelah ISBN dan data penerbit final tersedia.

## Lisensi

Hak cipta materi buku tetap dimiliki oleh penulis.

Lisensi kode sumber dapat ditentukan secara terpisah melalui file `LICENSE` pada repositori. Sebelum menggunakan kode untuk distribusi ulang atau penggunaan komersial, periksa lisensi yang berlaku pada repositori.

## Penulis

- Oddy Virgantara Putra
- Moch. Nasheh Annafii
- Triana Harmini
- Wahid Alfaridsi Achmad Zein

## Tautan

**Repositori:**  
https://github.com/virgantara/Metode-Numerik

---

Repositori ini dikembangkan sebagai pendamping buku agar pembaca tidak hanya memahami rumus, tetapi juga dapat **menjalankan, menguji, membandingkan, dan mengeksplorasi metode numerik secara langsung**.
