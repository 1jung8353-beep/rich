import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="OneBot Dashboard", layout="wide")

# 사이드바 메뉴
st.sidebar.title("OneBot Controls")
selected_page = st.sidebar.radio("Navigate", ["Home", "Trading", "Analytics", "Settings"])

# ----------------- HOME -----------------
if selected_page == "Home":
    st.title("🏠 OneBot Dashboard - Home")
    st.write("Welcome to OneBot! This is your control center.")

    # 더미 데이터
    balance = 1250
    growth = 5.3
    active_trades = 3

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Current Balance (USDT)", value=f"{balance:,}", delta=f"{growth}%")
    with col2:
        st.metric(label="Active Trades", value=active_trades, delta="+2")

# ----------------- TRADING -----------------
elif selected_page == "Trading":
    st.title("📈 Trading Overview")

    # 더미 가격 데이터
    df = pd.DataFrame({
        "Date": pd.date_range(datetime.date.today() - datetime.timedelta(days=30), periods=30),
        "Price": np.round(np.random.randn(30).cumsum() + 100, 2)
    })

    st.subheader("Market Price")
    st.line_chart(df.set_index("Date"))

    # 액션 버튼
    st.subheader("Trade Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Buy"):
            st.success("✅ Buy order placed at current price")
    with col2:
        if st.button("🔻 Sell"):
            st.error("❌ Sell order placed at current price")

    # 거래 내역
    st.subheader("Trade History")
    trade_data = pd.DataFrame({
        "Date": pd.date_range(datetime.date.today() - datetime.timedelta(days=5), periods=5),
        "Action": ["Buy", "Sell", "Buy", "Sell", "Buy"],
        "Price": np.round(np.random.randn(5).cumsum() + 100, 2),
        "Amount": [0.1, 0.2, 0.15, 0.1, 0.3]
    })
    st.table(trade_data)

# ----------------- ANALYTICS -----------------
elif selected_page == "Analytics":
    st.title("📊 Performance Analytics")

    # 더미 성과 데이터
    perf = pd.DataFrame({
        "Month": pd.date_range("2024-01-01", periods=12, freq="M").strftime("%b"),
        "PnL (%)": np.random.randint(-10, 20, 12)
    })

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Monthly PnL (%)")
        st.bar_chart(perf.set_index("Month"))
    with col2:
        st.subheader("Cumulative Growth")
        perf["Cumulative"] = perf["PnL (%)"].cumsum()
        st.line_chart(perf.set_index("Month")["Cumulative"])

    st.subheader("Key Stats")
    st.write(f"✅ Win Rate: {np.random.randint(50,80)}%")
    st.write(f"📈 Max Drawdown: {np.random.randint(-15,-5)}%")
    st.write(f"💰 Sharpe Ratio: {round(np.random.uniform(0.5,2.0),2)}")

# ----------------- SETTINGS -----------------
elif selected_page == "Settings":
    st.title("⚙️ Settings")

    st.subheader("API Configuration")
    api_key = st.text_input("Enter your API Key", type="password")
    secret_key = st.text_input("Enter your Secret Key", type="password")

    if st.button("Save Settings"):
        if api_key and secret_key:
            st.success("✅ API Keys saved successfully!")
        else:
            st.error("❌ Please enter both API and Secret keys.")

    st.subheader("Bot Settings")
    trade_size = st.slider("Default Trade Size (USDT)", 10, 1000, 100)
    leverage = st.slider("Leverage", 1, 20, 5)

    st.write(f"🔧 Current Config → Trade Size: {trade_size} USDT | Leverage: {leverage}x")
