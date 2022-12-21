import pickle
import streamlit as st

model_jantung = pickle.load(open('gagaljantung-model.sav', 'rb'))
st.title('Support Vector Machine Untuk Prediksi Resiko Gagal Jantung')

age = st.text_input('Berapa Umur Anda ?')
anaemia = st.text_input('Memiliki Anemia ? (0=tidak,1=ya)')
creatinine_phosphokinase = st.text_input('Level CPK darah')
diabetes = st.text_input('Memiliki Diabetes ? (0=tidak, 1=ya)')
ejection_fraction = st.text_input('Presentasi ejaction fraction')
high_blood_pressure = st.text_input(
    'Memiliki tekanan darah tinggi ? (0=tidak, 1=ya)')
platelets = st.text_input('Jumlah Platelets')
serum_creatinine = st.text_input('Level serum creatinine')
serum_sodium = st.text_input('Level serum sodium')
sex = st.text_input('Jenis kelamin (0=wanita, 1=pria)')
smoking = st.text_input('Apakah anda perokok ? (0=tidak, 1=ya)')
time = st.text_input('Follow-up period')

heartfail_diag = ' '

if st.button('Prediksi SEKARANG'):
    heartfail_pred = model_jantung.predict([[age, anaemia, creatinine_phosphokinase, diabetes,
                                             ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])
    if(heartfail_pred == 0):
        heartfail_diag = 'Pasien Relatif Tidak Beresiko Gagal Jantung'
        st.success(heartfail_diag)
    else:
        heartfail_diag = 'Pasien Relatif Beresiko Gagal Jantung'
        st.warning(heartfail_diag)
