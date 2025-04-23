### Introduction to Streamlit

import streamlit as st 

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interative app")
st.write("Choose your favourite vareity of chai")

chai=st.selectbox("Your favourite chai: ",["Masala chai","Lemon Tea","Adrak chai","Kesar chai"])
st.write(f"Your choose {chai}.Excellant choice")

st.success("Your chai has been brewed")

