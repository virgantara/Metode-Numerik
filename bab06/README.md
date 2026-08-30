# Bab 06 — Integrasi Numerik

Kode pendamping Bab 6 buku **Metode Numerik**.

## Isi folder

| File | Isi |
|---|---|
| `01_trapesium_komposit.py` | Aturan Trapesium komposit untuk fungsi analitik |
| `02_trapesium_data.py` | Integrasi data diskret tidak seragam dengan Trapesium |
| `03_simpson_komposit.py` | Aturan Simpson 1/3 komposit |
| `04_perbandingan_metode.py` | Perbandingan Trapesium dan Simpson dengan nilai analitik |
| `05_visualisasi_galat.py` | Grafik galat terhadap jumlah subinterval |
| `06_verifikasi_scipy.py` | Verifikasi integral menggunakan `scipy.integrate.quad()` |
| `07_studi_kasus_robin.py` | Estimasi luas teluk berdasarkan data diskret |

## Instalasi

```bash
python -m pip install -r requirements.txt
```

## Menjalankan contoh

```bash
python 01_trapesium_komposit.py
python 02_trapesium_data.py
python 03_simpson_komposit.py
python 04_perbandingan_metode.py
python 05_visualisasi_galat.py
python 06_verifikasi_scipy.py
python 07_studi_kasus_robin.py
```

Kode dibuat untuk tujuan pembelajaran. Mahasiswa dianjurkan membandingkan
hasil numerik dengan nilai analitik atau pustaka ilmiah ketika referensi tersedia.
