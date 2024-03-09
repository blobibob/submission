import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from datetime import datetime

# Load data 
# kalau terdapat error, hapus submission\, ganti jadi dashboard\day_clean.csv
day_df = pd.read_csv("dashboard\day_clean.csv")
hour_df = pd.read_csv("dashboard\hour_clean.csv")

# Navbar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Pertanyaan 1", "Pertanyaan 2"])

# Informasi
st.sidebar.title("Informasi")
st.sidebar.write("Nama: Clarissa Luna Maheswari")
st.sidebar.write("Email: clrsslunaaa@gmail.com")
st.sidebar.write("ID Dicoding: clrssluna")

# Link GitHub
st.sidebar.title("GitHub Repository")
st.sidebar.write("[Proyek Analisis Data](https://github.com/blobibob/submission)")

# Judul dan Konten Utama
st.title('Proyek Analisis Data')

# Pertanyaan 1: Apakah jumlah sewa sepeda dipengaruhi oleh waktu dalam sehari?
if selection == "Pertanyaan 1":
    st.header('Pertanyaan 1: Apakah jumlah sewa sepeda dipengaruhi oleh waktu dalam sehari?')
    st.write('Grafik di bawah ini menunjukkan adanya perbedaan dalam permintaan sepeda pada setiap jam dalam sehari. Permintaan sepeda tertinggi terjadi pada jam 17:00, sementara permintaan terendah terjadi pada jam 4:00 pagi.')

    fig, ax = plt.subplots(figsize=(10, 6))
    hourly_rentals = hour_df.groupby('hr')['cnt'].mean().reset_index()
    ax.plot(hourly_rentals['hr'], hourly_rentals['cnt'], marker='o')
    ax.set_xlabel('Jam dalam Sehari')
    ax.set_ylabel('Jumlah Penyewaan Sepeda (Rata-rata)')
    ax.set_title('Permintaan Sepeda pada Setiap Jam dalam Sehari')
    ax.set_xticks(np.arange(0, 24, 1))
    ax.grid(True)
    st.pyplot(fig)

    st.header('Conclution Pertanyaan 1:')
    st.write('Grafik distribusi jumlah penyewaan sepeda menunjukkan adanya perbedaan permintaan sepeda pada setiap jam dalam sehari.')
    st.write('Permintaan sepeda cenderung rendah pada jam-jam pagi (terendah sekitar jam 4 pagi) dan meningkat secara signifikan pada sore hari (tertinggi sekitar jam 5 sore).')
    st.write('Hal ini menunjukkan bahwa waktu mempengaruhi permintaan sepeda, dengan puncak permintaan terjadi saat jam pulang kerja.')

# Pertanyaan 2: Apakah terdapat perubahan jumlah penyewaan sepeda saat hari libur atau akhir pekan?
elif selection == "Pertanyaan 2":
    st.header('Pertanyaan 2: Apakah terdapat perubahan jumlah penyewaan sepeda saat hari libur atau akhir pekan?')
    st.write('Grafik di bawah ini memperlihatkan distribusi jumlah penyewaan sepeda pada hari kerja dan hari libur. Dari histogram tersebut, terlihat bahwa distribusi jumlah penyewaan sepeda pada hari kerja dan hari libur memiliki pola yang berbeda.')

    # Hitung total penyewaan sepeda per hari
    daily_rentals = hour_df.groupby('date')['cnt'].sum().reset_index()

    # Identifikasi hari kerja dan hari libur
    working_days = day_df[day_df['workingday'] == 1]['date']
    holidays = day_df[day_df['workingday'] == 0]['date']

    # Pisahkan data penyewaan sepeda berdasarkan hari kerja dan hari libur
    rentals_working_days = daily_rentals[daily_rentals['date'].isin(working_days)]['cnt']
    rentals_holidays = daily_rentals[daily_rentals['date'].isin(holidays)]['cnt']

    # Visualisasi menggunakan Seaborn
    plt.figure(figsize=(10, 6))
    sns.histplot(rentals_working_days, bins=20, alpha=0.5, label='Hari Kerja', kde=True, color='blue')
    sns.histplot(rentals_holidays, bins=20, alpha=0.5, label='Hari Libur', kde=True, color='orange')
    plt.xlabel('Jumlah Penyewaan Sepeda')
    plt.ylabel('Frekuensi')
    plt.title('Distribusi Jumlah Penyewaan Sepeda pada Hari Kerja dan Hari Libur')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

    st.header('Conclution Pertanyaan 2:')
    st.write('Analisis statistik menunjukkan bahwa rata-rata jumlah penyewaan sepeda pada hari kerja dan hari libur memiliki perbedaan yang cukup signifikan.')
    st.write('Jumlah penyewaan sepeda cenderung lebih tinggi pada hari kerja daripada hari libur.')
    st.write('Dengan demikian, dapat disimpulkan bahwa waktu dalam sehari berpengaruh terhadap permintaan sepeda, sementara terdapat perbedaan jumlah penyewaan sepeda antara hari kerja dan hari libur.')
