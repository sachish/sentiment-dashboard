
import streamlit as st
from sentiment_logic import get_sentiment_data
from telegram_alert import send_telegram_alert

st.set_page_config(page_title="Sentiment Dashboard", layout="wide")

st.title("📈 Options Sentiment Dashboard")
data = get_sentiment_data()

st.dataframe(data)

# Alert section
if st.button("Run Scan & Send Alerts"):
    matches = data[data['Signal'].isin(["CALL", "PUT", "EQUITY+"])]
    if not matches.empty:
        send_telegram_alert(matches)
        st.success("Alert sent via Telegram!")
    else:
        st.info("No actionable signals found.")
