import streamlit as st

#if 'button_clicked' not in st.session_state:
    #st.session_state.button_clicked = False

def handle_click():
    st.session_state.button_clicked = True

if st.button("Click me", on_click=handle_click):
    if not st.session_state.button_clicked:
        # Code to run only once on button click
        st.write("Button clicked for the first time!")
