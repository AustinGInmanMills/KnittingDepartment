import streamlit as st

placeholder = st.empty()

def page1():
    with placeholder.form("Hey"):
    submit = st.form_submit_button("click1")
    if submit: 
        st.write("hey")
        st.session_state.run = True
        
def page2():
    with placeholder.form("Bye"):
    submit = st.form_submit_button("click1")
    if submit: 
        st.write("hey")
        st.session_state.run = True

if not "run" in st.session_state:
    page1()
else:
    page2()
    

