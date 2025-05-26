# 🧵 ETL Pipeline - Fashion Product Scraper

Proyek ini membangun pipeline ETL (Extract, Transform, Load) untuk mengekstrak data produk fashion dari situs [fashion-studio.dicoding.dev](https://fashion-studio.dicoding.dev), membersihkan dan mentransformasikannya, lalu menyimpannya ke dalam file CSV dan Google Sheets.

---

## 📁 Struktur Proyek

```
ETL-Pipeline-DBS/
├── extract.py               # Modul ekstraksi data dari website
├── transform.py             # Modul transformasi dan pembersihan data
├── load.py                  # Modul penyimpanan ke CSV dan Google Sheets
├── main.py                  # Skrip utama untuk menjalankan pipeline ETL
├── products.csv             # Hasil data akhir dalam format CSV
├── tests/
│   ├── test_extract.py      # Unit test untuk ekstraksi
│   ├── test_transform.py    # Unit test untuk transformasi
│   └── test_load.py         # Unit test untuk penyimpanan
├── google-sheets-api.json   # File kredensial Google Sheets API
├── submission.txt           # Panduan menjalankan project
└── README.md                # Dokumentasi proyek ini
```

---

## 🚀 Cara Menjalankan

### 1. Instalasi Dependensi

Aktifkan virtual environment, lalu jalankan:

```bash
pip install -r requirements.txt
```

### 2. Menjalankan Skrip ETL

Jalankan pipeline dengan:

```bash
python main.py
```

Skrip ini akan:

* Mengekstrak data dari 50 halaman (total 1000 produk)
* Melakukan transformasi dan pembersihan
* Menyimpan hasil ke `products.csv` dan Google Sheets

---

## ✅ Menjalankan Unit Test

Untuk menjalankan semua unit test:

```bash
python -m pytest tests
```

---

## 📊 Menjalankan Test Coverage

Untuk melihat cakupan pengujian unit:

```bash
coverage run -m pytest tests
coverage report -m
```

---

## 📄 Hasil Output

* **File CSV**: `products.csv`
* **Google Sheets**:
  [https://docs.google.com/spreadsheets/d/1m84h2vohzMVctjWTbGHviMpFyCsBhGHvumKajifGGaA/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1AbCdEfGhIjKlMnOpQrStUvWxYz1234567890/edit#gid=0)


---

## 🛠 Teknologi yang Digunakan

* `requests`, `BeautifulSoup` – untuk Web Scraping
* `pandas` – untuk transformasi data
* `google-api-python-client` – untuk integrasi Google Sheets
* `pytest`, `coverage` – untuk unit testing dan laporan cakupan

---

## 👤 Kontributor

**M. Alwan Fauzi**

---
