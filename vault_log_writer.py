import json
import requests
import subprocess
from datetime import datetime

# === Wallet Settings ===
wallet_address = "0xA284B3499d4fC3dB457233b3dF476Cc15677CcAd"  # Replace with yours
eth_api_url = f"https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
eth_balance = 0.0053  # Static example, can replace with dynamic fetch if needed

# === Git Commit Data ===
commit = subprocess.check_output(["git", "log", "-1", "--pretty=format:%H||%an||%s||%ct"]).decode("utf-8")
commit_hash, author, message, timestamp = commit.split("||")

# === ETH Price Fetch ===
response = requests.get(eth_api_url)
eth_price = response.json()["ethereum"]["usd"]
usd_value = round(float(eth_balance) * eth_price, 2)

# === Vault Entry ===
entry = {
    "hash": commit_hash,
    "author": author,
    "message": message,
    "timestamp": timestamp,
    "logged_at": datetime.utcnow().isoformat() + "Z",
    "wallet_address": wallet_address,
    "eth_price": eth_price,
    "eth_balance": eth_balance,
    "usd_equivalent": usd_value
}

# === Log Write ===
log_file = "vault_log.json"

try:
    with open(log_file, "r") as f:
        logs = json.load(f)
    if not isinstance(logs, list):
        logs = [logs]
except:
    logs = []

logs.append(entry)

with open(log_file, "w") as f:
    json.dump(logs, f, indent=4)

print("✅ Vault updated with Git + ETH data.")
