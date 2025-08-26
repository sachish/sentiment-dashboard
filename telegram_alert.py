import requests

# Replace these with your actual credentials
bot_token = "8291039527:AAH6T3UN5lIllWjsb7EvLFdK27Q_znxFcYw"
chat_id = "1111326679"

def send_telegram_alert(df):
    for _, row in df.iterrows():
        message = (
            f"📢 {row['Signal']} ALERT: {row['Ticker']}\n"
            f"RSI: {row['RSI']} | P/C: {row['Put/Call']} | IV: {row['IV Trend']}\n"
            f"MA Pullback: {'Yes' if row['MA Pullback'] else 'No'}"
        )
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": message})


def send_test_alert():
    message = (
        "🚨 TEST ALERT 🚨\n"
        "Ticker: AAPL\n"
        "Signal: CALL\n"
        "RSI: 65 | P/C: 0.88 | IV: Rising\n"
        "MA Pullback: Yes"
    )
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    response = requests.post(url, data={"chat_id": chat_id, "text": message})
    print("Response:", response.status_code, response.text)

