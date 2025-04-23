### Layouts and Styling

import streamlit as st 

st.title("Chai Taste Poll")

col1, col2 =st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/5946623/pexels-photo-5946623.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
             width=200)
    vote1=st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/31739573/pexels-photo-31739573/free-photo-of-iced-milk-tea-with-jelly-and-lemon-iced-tea.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
             width=200)
    Vote2= st.button("Vote for Adrak Chai")
    
if vote1: 
    st.success("Thanks for voting masala chai")
elif Vote2:
    st.success("Thanks for voting adrak chai")
    
name= st.sidebar._text_input("Enter your name")
tea= st.sidebar.selectbox("Choose your chai", ["Masala","kesar","Adrak"])


st.write(f"welcome {name} and your {tea} chai is getting ready")

with st.expander("Show chai making instructions"):
    st.write("""
             1. Boil water with milk
             2. Add milk and spices
             3. Serve hot
             """)
    
st.markdown('### WELCOME TO CHAI APP')
st.markdown('> Blockquote')

    


    
    