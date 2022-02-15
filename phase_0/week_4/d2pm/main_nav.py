import data_viz, hypo
import streamlit as st

PAGES = {
    'Data Visualization': data_viz,
    'Hypothesis Testing': hypo
}

selection = st.sidebar.selectbox("select a page", list(PAGES.keys()))

page = PAGES[selection]

page.app() #data_viz.app() / hypo.app()
