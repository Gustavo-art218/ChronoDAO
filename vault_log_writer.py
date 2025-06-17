import json

data = {
    "wallet_address": "0xA284B3499d4FC3dB457233b3dF476Cc15677cCAd",
    "eth_price": 2568.13,
    "eth_balance": 0.0053,
    "usd_equivalent": 13.67
}

with open("vault_log.json", "w") as file:
    json.dump(data, file, indent=4)

print("✅ Vault log written successfully.")
