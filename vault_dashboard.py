import streamlit as st
import json

# 🔓 Load the vault data from JSON
with open("vault_log.json", "r") as file:
    logs = json.load(file)

# ✅ Validate data structure
if isinstance(logs, list) and len(logs) > 0:
    latest = logs[-1]  # Grab most recent log entry
else:
    st.error("🚫 No data found in vault_log.json.")
    st.stop()

# 🧱 UI Layout
st.set_page_config(page_title="ChronoDAO Vault UI", layout="centered")
st.title("🔐 ChronoDAO Vault Dashboard")

# 📈 Metrics Display
st.subheader("📊 ETH Price")
st.metric("Price (USD)", f"${latest['eth_price']}")

st.subheader("💰 Wallet Info")
st.write(f"**Address**: `{latest.get('wallet_address', 'N/A')}`")
st.metric("Balance", f"{latest['eth_balance']} ETH")
st.metric("USD Equivalent", f"${latest['usd_value']}")

st.success("🔥 Vault protocol is live.")
