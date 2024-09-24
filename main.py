import streamlit as st

def page1():
    placeholder = st.empty()
    with placeholder.form("Bye"):
        if st.form_submit_button:
            st.write("Bye")
            time.sleep(3)
            placeholder.empty()
            page2()
    
def page2():
    placeholder = st.empty()
    with placeholder.form("Hello"):
        if st.form_submit_button:
            st.write("Hello")
            
            
page1()