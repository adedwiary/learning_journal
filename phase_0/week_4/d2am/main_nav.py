import viz
import hypo
import streamlit as st

PAGES = {
    'Data Visualization': viz,
    'Hypothesis Testing': hypo
}

selection = st.sidebar.selectbox('Select a page: ', list(PAGES.keys()))

page = PAGES[selection]

page.app() #viz.app() / hypo.app()