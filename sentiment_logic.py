
import pandas as pd
import yfinance as yf

def get_sentiment_data():
    tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "JPM", "V", "UNH", "NFLX"]
    rows = []

    for ticker in tickers:
        data = yf.Ticker(ticker).history(period="5d")
        rsi = data['Close'].pct_change().rolling(14).mean().iloc[-1] * 100 + 50  # Mock RSI
        # Mock options data
        put_call = 1.2 if ticker in ["NVDA", "TSLA"] else 0.8
        oi_ratio = 2.0 if ticker in ["NVDA"] else 0.9
        iv_trend = "Rising" if ticker in ["AAPL", "NVDA"] else "Neutral"
        ma_pullback = True if abs(data['Close'].iloc[-1] - data['Close'].rolling(50).mean().iloc[-1]) < 2 else False

        signal = "-"
        if rsi > 60 and put_call < 1 and iv_trend == "Rising":
            signal = "CALL"
        elif rsi < 50 and put_call > 1.5 and oi_ratio > 1.5:
            signal = "PUT"
        elif ma_pullback and rsi > 50 and iv_trend == "Rising":
            signal = "EQUITY+"

        rows.append({
            "Ticker": ticker,
            "RSI": round(rsi, 2),
            "Put/Call": put_call,
            "OI Ratio": oi_ratio,
            "IV Trend": iv_trend,
            "MA Pullback": ma_pullback,
            "Signal": signal
        })

    return pd.DataFrame(rows)
