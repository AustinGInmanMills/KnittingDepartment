import streamlit as st

def page2():
    st.title("Second page")

pg = st.navigation([
    st.Page("main.py", title="First page", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
])
pg.run()