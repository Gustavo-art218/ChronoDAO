import streamlit as st
import json

# Load the vault data (list of logs)
with open("vault_log.json", "r") as file:
    data = json.load(file)

latest = data[-1]  # Grab most recent entry

st.set_page_config(page_title="ChronoDAO Vault UI", layout="centered")

st.title("🔐 ChronoDAO Vault Dashboard")

st.subheader("📈 ETH Price")
st.metric("Price (USD)", f"${latest['eth_price']}")

st.subheader("💰 Wallet Info")
st.metric("Balance", f"{latest['eth_balance']} ETH")
st.metric("USD Equivalent", f"${latest['usd_value']}")

st.success("🔥 Vault protocol is live.")
