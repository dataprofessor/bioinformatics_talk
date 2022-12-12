import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(page_title="Bioinformatics talk", page_icon="🧬")

# Streamit book properties
stb.set_book_config(path="slides")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.markdown('''
# About this Talk
In this talk, I share some of my thought process that I have accrued over the years building bioinformatics tools for computational drug discovery.

# About the Speaker
<div style="float:left">
<img src="https://github.com/dataprofessor/bioinformatics_talk/blob/master/images/chanin.png?raw=true" width=35%>
</div>
Chanin is a Senior Developer Advocate for Streamlit at Snowflake Inc. In his spare time, he creates educational content on data science, coding and bioinformatics on his YouTube channel [Data Professor](https://youtube.com/dataprofessor).

In his previous career, he worked in academia for 15 years. His recent position was Associate Professor of Bioinformatics and the Head of the Center of Data Mining and Biomedical Informatics, Faculty of Medical Technology, Mahidol University.

''', unsafe_allow_html=True)
