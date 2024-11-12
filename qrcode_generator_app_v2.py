import streamlit as st
from decode_qrcode_page import decode_qrcode_page
from generate_qrcode_page import generate_qrcode

# Using object notation
choice = st.sidebar.selectbox(
    "Menu",
    ("Create QR Code", "Decode QR Code", "About me")
)

if choice == "Create QR Code":
    generate_qrcode()
elif choice == "Decode QR Code":
    decode_qrcode_page()
elif choice == "About me":
    st.write("Hi! My name is maryam")