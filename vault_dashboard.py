import streamlit as st
import json

# ✅ FIRST Streamlit command
st.set_page_config(page_title="ChronoDAO Vault UI", layout="centered")

st.title("🔐 ChronoDAO Vault Dashboard")
st.subheader("🧠 Git Commit Feed")

with open("vault_log.json", "r") as f:
    logs = json.load(f)

latest = logs[-1] if isinstance(logs, list) else logs
st.json(latest)

# 🧮 Metrics Display
st.subheader("📊 ETH Price")
st.metric("Price (USD)", f"${latest['eth_price']}")

st.subheader("👛 Wallet Info")
st.write(f"**Address**: `{latest.get('wallet_address', 'N/A')}`")
st.metric("Balance", f"{latest['eth_balance']} ETH")
st.metric("USD Equivalent", f"${latest['usd_equivalent']}")

st.success("🔥 Vault protocol is live.")
