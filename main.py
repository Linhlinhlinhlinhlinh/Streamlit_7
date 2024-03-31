import streamlit as st
st.set_page_config(page_title="BFF", page_icon='💖', layout='wide')
st.title("Hay nhap ten nhung bff cua ban")
name = st.text_input('Hay nhap ten bff cua ban')
gender = st.text_input('Hay nhap gioi tinh cua ban')
age = st.text_input('Hay nhap tuoi cua ban')
if name != '' and gender != '' and age != '':
  s = st.button('NEXT')
else:
  st.warning('Vui long nhap day du thong tin')
if 's' in locals():
  if s :
    st.text('NEXT button clicked')
