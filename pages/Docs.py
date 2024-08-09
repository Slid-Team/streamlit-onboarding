import streamlit as st

st.set_page_config(page_title="Docs", page_icon="📈")

with open("README.md", "r", encoding="utf-8") as f:
    st.markdown(f.read())
