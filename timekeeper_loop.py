print("🕰️ Timekeeper ritual initialized.")

for i in range(5):
    print(f"🔁 Scroll {i + 1} activated.")

print("⏱️ All scrolls cast. Awaiting next cycle.")
eth_prices = [3710, 3742, 3688, 3795, 3821]

for price in eth_prices:
    if price > 3750:
        print(f"📈 ETH price spike detected: ${price}")
    else:
        print(f"💤 ETH stable at ${price}")
