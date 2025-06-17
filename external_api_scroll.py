import requests

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data["ethereum"]["usd"]
    print(f"🔮 Current ETH Price: ${price}")

get_eth_price()

