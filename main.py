import numpy as np, pandas as pd, streamlit as st 
from streamlit_option_menu import option_menu 
 
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected


# if selected == "Home":
#    st.title (f"You have selected  {selected}")
# elif selected == "Project":
#   st.title(f"You have selected {selected}")
# else:
#   st.title(f"You have selected {selected}")

selected_choice = ["Log In", "Sign up"]
choice  = st.selectbox("", options = selected_choice)
#if st.session_state: 
with st.form ("Wellcome"):  
    if choice == "Sign up":
      st.text_input("Enter email address")
      st.text_input("Enter user name")
      st.text_input("Enter password")
    else:
      st.text_input("Enter user name")
      st.text_input("Enter password")
    st.form_submit_button("Submit")

st.divider()
st.write("New content")


 


