import streamlit as st
import requests

# Set page title
st.set_page_config(page_title="Currency Converter", page_icon="💰")

st.title("Currency Converter 💰")
st.write("Convert currencies using real-time exchange rates!")

# User inputs
amount = st.number_input("Enter Amount:", min_value=0.01, step=0.01, value=1.00)
from_currency = st.text_input("From Currency (e.g., USD):", "USD").upper()
to_currency = st.text_input("To Currency (e.g., INR):", "INR").upper()


API_URL = "https://flask-currency-api-2.onrender.com/convert"  # flask API

if st.button("Convert"):
    params = {"amount": amount, "from": from_currency, "to": to_currency}
    response = requests.get(API_URL, params=params).json()

    if "error" in response:
        st.error("Invalid currency code!")
    else:
        st.success(f"{amount} {from_currency} = {response['converted_amount']} {to_currency}")

st.markdown(
    """
    <style>
    .stApp {
        background-color: purple !important; /* Light Gray */
    }
    .stMarkdown, .stTitle, .stHeader, .stText {
        color: aqua !important; /* Black text */
    }
    </style>
    """,
    unsafe_allow_html=True
)