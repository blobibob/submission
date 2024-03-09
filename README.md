# Panduan Menjalankan Aplikasi Analisis Data dengan Streamlit

Aplikasi ini memungkinkan pengguna untuk menganalisis data sepeda menggunakan Python dan berbagai library seperti Pandas, Matplotlib, Seaborn, dan Streamlit.

## Langkah-langkah untuk Menjalankan Aplikasi:

1. **Persiapan:**
   - Pastikan Python telah terinstal di komputer.

2. **Instalasi Library yang Diperlukan:**
   - Pastikan semua library yang diperlukan telah diinstal. Gunakan pip dengan perintah berikut:
     ```bash
     pip install numpy pandas matplotlib seaborn streamlit babel
     ```

3. **Menyimpan File Python dan Data:**
   - Simpan file Python `dashboard.py` di komputer. Pastikan juga ada dua file data, yaitu `day_clean.csv` dan `hour_clean.csv`, dalam direktori yang sama dengan file Python.

4. **Jalankan Aplikasi dengan Streamlit:**
   - Buka terminal atau command prompt, arahkan ke direktori tempat menyimpan file Python, lalu jalankan aplikasi dengan perintah:
     ```bash
     streamlit run dashboard.py
     ```

5. **Navigasi Halaman:**
   - Setelah menjalankan perintah tersebut, aplikasi akan berjalan dan tampil di browser. Navigasi di samping kiri memungkinkan pengguna memilih antara "Pertanyaan 1" dan "Pertanyaan 2".

6. **Pilih Pertanyaan:**
   - Klik pada salah satu opsi pertanyaan untuk melihat visualisasi dan kesimpulan terkait pertanyaan tersebut.

Dengan mengikuti langkah-langkah di atas, pengguna akan dapat menjalankan aplikasi analisis data menggunakan Streamlit dan menjelajahi hasil analisisnya.
