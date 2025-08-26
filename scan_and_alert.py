
from sentiment_logic import get_sentiment_data
from telegram_alert import send_telegram_alert

def run_scan():
    df = get_sentiment_data()
    matches = df[df['Signal'].isin(["CALL", "PUT", "EQUITY+"])]
    if not matches.empty:
        send_telegram_alert(matches)
        print("✅ Alerts sent.")
    else:
        print("ℹ️ No signals found.")

if __name__ == "__main__":
    run_scan()
