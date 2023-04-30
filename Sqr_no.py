import streamlit as st
num = st.slider("Choose ur number: ",1,100)
st.write('Square of ', num, 'is', num**2)