import streamlit as st
import requests

# Function to get exchange rates
def get_exchange_rate(from_currency, to_currency):
    api_key = "YOUR_API_KEY"  # Replace with actual API Key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url).json()
    
    if response["result"] == "success":
        return response["conversion_rates"].get(to_currency, None)
    return None

# UI Design
st.set_page_config(page_title="Currency Converter", page_icon="💰", layout="wide")

# Sidebar Theme Selection
with st.sidebar:
    st.markdown("### 🌙 Choose Theme:")
    theme = st.radio("", ["Light", "Dark"], horizontal=True)

    # Quick Access Links
    st.markdown("### 🔍 Quick Access")
    st.markdown("- *Unit Conversion* ")
    st.markdown("- *Currency Exchange*")

# Apply CSS for Background Styling
st.markdown(
    """
    <style>
    .main { background: linear-gradient(to right, #B5C0D0, #D9A7C7); }
    </style>
    """,
    unsafe_allow_html=True,
)

# Currency Converter Section
st.markdown("## 💰 Currency Conversion")
amount = st.number_input("Amount", min_value=0.00, step=1.0, format="%.2f")
from_currency = st.selectbox("From Currency", ["USD", "EUR", "GBP", "INR", "PKR", "AUD", "CAD"])
to_currency = st.selectbox("To Currency", ["USD", "EUR", "GBP", "INR", "PKR", "AUD", "CAD"])

if st.button("Convert Currency", use_container_width=True):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    if exchange_rate:
        converted_amount = round(amount * exchange_rate, 2)
        st.success(f"{amount} {from_currency} = {converted_amount} {to_currency}")
    else:
        st.error("Error fetching exchange rate. Try again later.")

# Currency Trends Section
st.markdown("## 📊 Currency Exchange Rate Trends")
if st.button("Show Currency Trend", use_container_width=True):
    st.info("Feature Coming Soon! 🚀")

