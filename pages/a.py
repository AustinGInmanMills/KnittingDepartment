import streamlit as st
st.write(st.query_params)
if "name" not in st.session_state:
    st.write("Name not found")
    name = st.query_params.names
else:
    name = st.session_state.name
    st.write(f"{st.session_state.name} found")


