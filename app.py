import streamlit as st
import pandas as pd
import numpy as np
import datetime

# 앱 타이틀
st.set_page_config(page_title="OneBot Dashboard", layout="wide")

# 사이드바
st.sidebar.title("⚙️ OneBot Controls")
selected_page = st.sidebar.radio("Navigate", ["Home", "Trading", "Analytics", "Settings"])

# 더미 데이터 생성 (추후 실시간 데이터로 교체)
dates = pd.date_range(datetime.date.today() - datetime.timedelta(days=30), periods=30)
prices = np.random.randn(30).cumsum() + 100
df = pd.DataFrame({"Date": dates, "Price": prices})

# 페이지별 UI
if selected_page == "Home":
    st.title("🏠 OneBot Dashboard - Home")
    st.write("Welcome to OneBot! This is your control center.")
    st.metric("Current Balance (USDT)", "1,250", "+5.3%")
    st.metric("Active Trades", "3", "▲")

elif selected_page == "Trading":
    st.title("📈 Trading Overview")
    st.line_chart(df.set_index("Date"))

    st.subheader("Trade Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Buy"):
            st.success("Buy order placed!")
    with col2:
        if st.button("🔻 Sell"):
            st.error("Sell order placed!")

elif selected_page == "Analytics":
    st.title("📊 Analytics")
    st.bar_chart(df.set_index("Date"))
    st.area_chart(df.set_index("Date"))

elif selected_page == "Settings":
    st.title("⚙️ Settings")
    st.text_input("API Key", type="password")
    st.text_input("API Secret", type="password")
    st.button("Save Settings")

# 푸터
st.sidebar.markdown("---")
st.sidebar.info("Powered by OneBot 🚀")
