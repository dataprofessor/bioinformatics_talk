import streamlit as st
import streamlit_book as stb
from PIL import Image

st.title('Towards the Development of Bioinformatics Tools')

cover_img = Image.open('images/bioinformatics-cover-image.png')
st.image(cover_img)

col1, col2 = st.columns(2)
with col1:
  st.write('R User Group')
  st.write('Harvard Data Science Initiative')
with col2:
  st.subheader('Chanin Nantasenamat, PhD')
  st.write('Streamlit Open Source, Snowflake Inc.')
