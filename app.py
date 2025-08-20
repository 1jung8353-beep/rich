import streamlit as st

# ----------------- SIDEBAR NAVIGATION -----------------
st.sidebar.title("OneBot Controls 🚀")
selected_page = st.sidebar.radio("Navigate", ["Home", "Trading", "Analytics", "Settings"])

# ----------------- HOME -----------------
if selected_page == "Home":
    st.title("🏠 OneBot Dashboard - Home")
    st.write("Welcome to OneBot! This is your control center.")

    st.metric(label="Current Balance (USDT)", value="1,250", delta="+5.3%")
    st.metric(label="Active Trades", value="3", delta="+2")

# ----------------- TRADING -----------------
elif selected_page == "Trading":
    st.title("📈 Trading Panel")
    st.write("Here you can monitor and manage your trades.")

    st.subheader("Open Positions")
    st.table({
        "Symbol": ["BTC/USDT", "ETH/USDT", "XRP/USDT"],
        "Side": ["Long", "Short", "Long"],
        "Size": ["0.01 BTC", "0.5 ETH", "1000 XRP"],
        "PnL": ["+$25", "-$10", "+$5"]
    })

    st.subheader("New Trade")
    trade_pair = st.text_input("Trading Pair", "BTC/USDT")
    trade_size = st.number_input("Trade Size (USDT)", 10, 10000, 100)
    direction = st.radio("Direction", ["Long", "Short"])

    if st.button("Execute Trade"):
        st.success(f"✅ Placed {direction} order on {trade_pair} with {trade_size} USDT")

# ----------------- ANALYTICS -----------------
elif selected_page == "Analytics":
    st.title("📊 Performance Analytics")
    st.line_chart({"PnL": [100, 250, 180, 300, 400, 350, 500]})
    st.bar_chart({"Win Rate %": [55, 60, 62, 58, 65]})

# ----------------- SETTINGS -----------------
elif selected_page == "Settings":
    st.title("⚙️ Settings")

    st.subheader("API Configuration (Bitget)")
    api_key = st.text_input("Enter your API Key", type="password")
    secret_key = st.text_input("Enter your Secret Key", type="password")
    passphrase = st.text_input("Enter your Passphrase", type="password")   # ✅ 추가됨

    if st.button("Save Settings"):
        if api_key and secret_key and passphrase:
            st.success("✅ API Keys saved successfully!")
        else:
            st.error("❌ Please enter API Key, Secret Key, and Passphrase.")

    st.subheader("Bot Settings")
    trade_size = st.slider("Default Trade Size (USDT)", 10, 1000, 100)
    leverage = st.slider("Leverage", 1, 20, 5)

    st.write(f"🔧 Current Config → Trade Size: {trade_size} USDT | Leverage: {leverage}x")
