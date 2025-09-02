from .price_fetcher import fetch_price_history, calculate_rsi, calculate_macd

def analyze_stock(symbol: str):
    df = fetch_price_history(symbol)

    if df.empty or 'Close' not in df:
        return {"error": "No valid data found."}

    df["RSI"] = calculate_rsi(df["Close"])
    macd, signal = calculate_macd(df["Close"])
    df["MACD"] = macd
    df["Signal"] = signal

    latest = df.iloc[-1]

    # 简单策略建议
    signal_msg = []

    if latest["RSI"] < 30:
        signal_msg.append("📉 超卖区：可能是买入机会")
    elif latest["RSI"] > 70:
        signal_msg.append("📈 超买区：注意风险，可能调整")

    if latest["MACD"] > latest["Signal"]:
        signal_msg.append("✅ MACD 金叉：短期看涨")
    else:
        signal_msg.append("⚠️ MACD 死叉：短期看跌")

    return {
        "symbol": symbol,
        "latest_date": str(latest["Date"].date()),
        "latest_close": float(latest["Close"]),
        "RSI": round(latest["RSI"], 2),
        "MACD": round(latest["MACD"], 4),
        "Signal": round(latest["Signal"], 4),
        "analysis": signal_msg
    }
