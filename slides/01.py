import streamlit as st
import streamlit_book as stb
from PIL import Image

st.title('Towards the Development of Bioinformatics Tools')

cover_img = Image.open('images/bioinformatics-cover-image.png')
st.image(cover_img)

col1, col2 = st.columns(2)
with col1:
  st.markdown('''
  <div style="font-size:24px; color:Gray">
        R User Group
      </div>
      <div style="font-size:18px; color:Gray"; vertical-align:bottom">
        Harvard Data Science Institute
  </div>
  ''', unsafe_allow_html=True)
with col2:
  st.markdown('''
  <div style="font-size:24px; text-align:right">
    <b>Chanin Nantasenamat, PhD</b>
  </div>
  <div style="font-size:18px; color:Gray; text-align:right">
    <i>Streamlit Open Source, Snowflake Inc.</i>
  </div>
  ''', unsafe_allow_html=True)
