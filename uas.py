import streamlit as st
import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from streamlit_option_menu import option_menu
import streamlit as st

#navigasi sidebar
# horizontal menu
selected2 = option_menu(None, ["Data", "Procecing data", "Modelling", 'Implementasi'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2

#halaman Data
if (selected2 == 'Data') :
    st.title('Deskripsi data')

    st.write("Ini adalah contoh data yang tersedia dalam aplikasi Streamlit.")
    st.write("Data ini dikumpulkan dari internet yang berasal dari sebuah perusahaan obat yang telah berlabel set data obat dan parameter yang mempengaruhinya. Oleh karena itu, berdasarkan penyakit dan jenis pasien, obat tersebut direkomendasikan.")
    st.write("Data ini diambil dari Kaggle")
    st.write("The target feature is")
    st.write("- Drug type")
    st.write("The feature sets are:")
    st.write("- Age")
    st.write("- Sex")
    st.write("- Blood Pressure Levels (BP)")
    st.write("- Cholesterol Levels")
    st.write("- Na to Potassium Ration")
    data = pd.read_csv('drug200.csv')
    st.write(data)



#halaman procecing data 
if (selected2 == 'Procecing data') :
    st.title('Procecing Data')

    st.write("Saya Melakukan Pre-processing data dengan metode Min - Max Scalar")
    st.write("Dengan Hasil Processing Data")
    data = pd.read_csv('drug_preprocessed.csv')
    st.write(data)

#halaman modelling
if (selected2 == 'Modelling'):
    st.title('Modelling')

    pilih = st.radio('Pilih', ('Naive Bayes', 'Decision Tree', 'KNN', 'ANN'))

    if (pilih == 'Naive Bayes'):
        st.title(' Nilai Akurasi 52,5 %')
    elif (pilih == 'Decision Tree'):
        st.title(' Nilai Akurasi 88 %')
    elif (pilih == 'KNN'):
        st.title(' Nilai Akurasi 77,5 %')
    elif (pilih == 'ANN'):
        st.title(' Nilai Akurasi 62,5%')


#halaman implementasi
# Load the saved model
if (selected2 == 'Implementasi'):
    st.title('Implementasi')

def calculate_risk(age, sex, blood_pressure, cholesterol, ratio, drug_type):
    # Lakukan perhitungan di sini sesuai dengan logika yang diperlukan
    # Misalnya, kamu dapat menggunakan algoritma atau rumus yang sesuai untuk menghitung risiko obat

    # Contoh sederhana untuk menunjukkan hasil perhitungan
    result = "Tipe obat"
    return result

def main():
    st.title("Drug Classification")

    # Buat input fields untuk menerima input dari pengguna
    age = st.number_input("Usia", min_value=1, max_value=100)
    sex = st.selectbox("Jenis Kelamin", ["Pria", "Wanita"])
    blood_pressure = st.number_input("Tingkat Tekanan Darah")
    cholesterol = st.number_input("Kolesterol")
    ratio = st.number_input("Rasio Na ke K")
    # drug_type = st.selectbox("Tipe Obat", ["DrugY", "drugX", "drugA", "drugC", "drugB"])

    # Buat tombol untuk memulai perhitungan saat ditekan
    if st.button("Hitung Risiko"):
        result = calculate_risk(age, sex, blood_pressure, cholesterol, ratio)
        st.write("Hasil Perhitungan:")
        st.write(result)

if __name__ == "__main__":
    main()

