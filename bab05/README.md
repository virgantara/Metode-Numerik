# Bab 05 — Diferensiasi Numerik

Kode pendamping Bab 5 buku **Metode Numerik**.

## Isi folder

| File | Isi |
|---|---|
| `01_roundoff_ukuran_langkah.py` | Eksperimen galat pembulatan saat `h` sangat kecil |
| `02_beda_hingga.py` | Beda maju, beda mundur, dan beda pusat |
| `03_richardson.py` | Ekstrapolasi Richardson untuk beda pusat |
| `04_variasi_h.py` | Eksperimen galat pada berbagai ukuran langkah |
| `05_visualisasi_galat.py` | Grafik log-log ukuran langkah terhadap galat |
| `06_diferensiasi_data_sensor.py` | Diferensiasi array data diskret berjarak seragam |
| `07_studi_kasus_chopper.py` | Studi kasus pemantauan laju perubahan suhu |

## Instalasi

```bash
python -m pip install -r requirements.txt
```

## Menjalankan contoh

```bash
python 01_roundoff_ukuran_langkah.py
python 02_beda_hingga.py
python 03_richardson.py
python 04_variasi_h.py
python 05_visualisasi_galat.py
python 06_diferensiasi_data_sensor.py
python 07_studi_kasus_chopper.py
```

Kode dibuat untuk tujuan pembelajaran. Mahasiswa dianjurkan membandingkan
hasil dengan turunan analitik ketika tersedia dan mengamati pengaruh ukuran
langkah serta noise terhadap galat diferensiasi.
