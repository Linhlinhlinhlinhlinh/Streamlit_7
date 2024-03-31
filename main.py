import streamlit as st
st.set_page_config(page_title="BFF", page_icon='💖', layout='wide')
st.title("Hay nhap ten nhung bff cua ban")
name = st.text_input('Hay nhap ten bff cua ban')
gender = st.selectbox('Hay nhap gioi tinh cua ban', ['Nam', 'Nu'])
