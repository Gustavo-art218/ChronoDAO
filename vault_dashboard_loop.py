import requests
import time

ETHERSCAN_API_KEY = "94WP3WNGDMTZKA4MX3W6WK1UZRMWGAAY1E"
wallet_address = "0xA284B3499d4FC3dB457233b3dF476Cc15677cCAd"  # your MetaMask

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data["ethereum"]["usd"]

def get_wallet_balance(address):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "1":
        eth_balance = int(data["result"]) / (10**18)
        return eth_balance
    else:
        return None

def run_loop(interval_seconds):
    print("⏱️ ChronoDAO Signal Loop Activated")
    while True:
        price = get_eth_price()
        balance = get_wallet_balance(wallet_address)
        usd_value = balance * price if balance else 0

        print("\n🔥 — SIGNAL UPDATE —")
        print(f"📈 ETH Price: ${price}")
        print(f"💰 Wallet Balance: {balance:.4f} ETH")
        print(f"💵 USD Equivalent: ${usd_value:,.2f}")
        print("🕰️ Waiting for next cycle...\n")

        time.sleep(interval_seconds)

# Start loop every 30 seconds
run_loop(30)
