import streamlit as st
num = st.slider("Choose ur number: ",1,100)
st.write('Cube of ', num, 'is', num**3)