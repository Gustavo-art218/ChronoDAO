import requests

ETHERSCAN_API_KEY = "94WP3WNGDMTZKA4MX3W6WK1UZRMWGAAY1E"
wallet_address = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe"  # test address

def get_wallet_balance(address):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "1":
        eth_balance = int(data["result"]) / (10**18)
        print(f"💰 Wallet Balance for {address}: {eth_balance:.4f} ETH")
    else:
        print("❌ Failed to fetch balance:", data['message'])

get_wallet_balance(wallet_address)
