import streamlit as st
import eda
import prediction as prediction

page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploratory Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page')
    st.image('https://www.epa.gov/sites/default/files/styles/medium/public/2021-05/aqaw_2021_0.png?itok=dMP6C0bR')
    st.write('Milestone 2')
    st.write('Nama      : Permata Hajjarianti')
    st.write('Batch     : HCK-011')
    st.write('Tujuan GC7 : Program kali ini dibuat untuk mengotomatisasi identifikasi yang penyakit Monkey Pox atau bukan melalui gambar.')
    st.write('')
    st.caption('Silahkan pilih menu di Select Box pada sebelah kiri layar anda!')
    st.write('')
    st.write('')

    with st.expander("Latar Belakang"):
            st.caption('''Dilansir dari Kementerian Kesehatan RI, gejala Monkey Pox hampir sama dengan cacar air, bahkan lebih ringan. Penderita akan mengalami demam, sakit kepala, nyeri otot, dan kelelahan. Bedanya, cacar monyet menyebabkan pembengkakan kelenjar getah bening, sedangkan cacar air tidak. Ahli juga mengingatkan bahwa Monkey Pox bisa menyebabkan gejala parah sampai komplikasi pada kelompok rentan.
                       Maka dari itu, perlu dilakukan identifikasi secara cepat dan tepat penyakit Monkey Pox sehingga penularannya tidak meluas dan mutasi virus penyebab Monkey Pox bisa diminimalkan. Dan bagi pasien yang terkena penyakit Monkey Pox dapat ditangani / diobati dengan tepat.
                       ''')



elif page == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()