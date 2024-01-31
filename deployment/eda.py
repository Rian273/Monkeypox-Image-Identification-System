import streamlit as st
from PIL import Image

def run():
    st.title('Welcome to EDA')


    st.subheader('Distribusi Data Train')
    image = Image.open('train distribution.png')
    st.image(image, caption='figure 1')

    with st.expander('Explanation'):
        st.caption('Pada data train terdapat 980 data Monkeypox dan 1162 data Others. Jumlah data pada kategori Others lebih banyak dibanding kategori Monkeypox.')


    st.subheader('Distribusi Data Test')
    image = Image.open('test distribution.png')
    st.image(image, caption='figure 2')

    with st.expander('Explanation'):
        st.caption('Pada data test terdapat 23 data Monkeypox dan 25 data Others. Jumlah data pada kategori Others lebih banyak dibanding kategori Monkeypox.')


    st.subheader('Distribusi Data Val')
    image = Image.open('val distribution.png')
    st.image(image, caption='figure 3')

    with st.expander('Explanation'):
        st.caption('Pada data validation terdapat 168 data Monkeypox dan 252 data Others. Jumlah data pada kategori Others lebih banyak dibanding kategori Monkeypox.')

    st.subheader('Sample Data')
    image = Image.open('monkeypox and others.png')
    st.image(image, caption='figure 5')

    with st.expander('Explanation'):
        st.caption('Dapat dilihat dari beberapa sample gambar di atas bahwa data sudah melakukan proses augmentasi sebelumnya. Dan diketahui ukuran gambar yaitu 224x224.')

if __name__ == "__name__":
     run()
