import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(page_title="Bioinformatics talk", page_icon="🧬")

# Streamit book properties
stb.set_book_config(path="slides")

st.markdown('''
<style>
div.block-container.css-12oz5g7.egzxvld2 {
    margin-top: 0em;
}
</style>''', unsafe_allow_html=True)

st.sidebar.header('About this talk')
st.sidebar.markdown('''
In this talk, I share some of my thought process that I have accrued over the years building bioinformatics tools for computational drug discovery.
''')
