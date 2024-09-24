import streamlit as st
st.write(st.query_params)
if "name" not in st.session_state:
    st.write("Name not found")
else:
    st.write(f"{st.session_state.name} found")


