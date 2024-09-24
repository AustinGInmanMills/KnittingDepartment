import streamlit as st

def page1():
    placeholder = st.empty()
    with placeholder.form("Bye"):
        if st.form_submit_button:
            st.write("Bye")
    
def page2():
    placeholder = st.empty()
    with placeholder.form("Hello"):
        if st.form_submit_button:
            st.write("Hello")
            
            
st.page(page2())