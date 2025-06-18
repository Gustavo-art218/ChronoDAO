import streamlit as st
import json

# 🧭 Set page layout
st.set_page_config(page_title="ChronoDAO Vault UI", layout="centered")

# 🔐 Title & Commit Feed
st.title("🔐 ChronoDAO Vault Dashboard")
st.subheader("🧠 Git Commit Feed")

with open("vault_log.json", "r") as f:
    logs = json.load(f)

latest = logs[-1] if isinstance(logs, list) else logs

# ✍️ Commit Summary
st.markdown(f"""
**Author**: `{latest.get("author", "")}`  
**Message**: `{latest.get("message", "")}`  
**Timestamp**: `{latest.get("timestamp", "")}`  
**Logged At**: `{latest.get("logged_at", "")}`
""")

# 📊 ETH Metrics
st.subheader("📊 ETH Price")
st.metric("Price (USD)", f"${latest.get('eth_price', 'N/A')}")

# 👛 Wallet Details
st.subheader("🍉 Wallet Info")
st.markdown(f"**Address**: `{latest.get('wallet_address', 'N/A')}`")
st.metric("Balance", f"{latest.get('eth_balance', 'N/A')} ETH")
st.metric("USD Equivalent", f"${latest.get('usd_equivalent', 'N/A')}")

# ✅ Final Signal
st.success("✅ Vault is LIVE and syncing.")
