#app.py
import app
import app2
import streamlit as st
PAGES = {
    "Steam API": app,
    "Epic Games API": app2
}
st.sidebar.title('Menu')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()