def summon_scroll(name, level):
    print(f"📜 Scroll '{name}' summoned at Level {level}.")

def price_alert(price):
    if price > 3750:
        print(f"📈 ETH Surge: ${price}")
    else:
        print(f"💤 ETH Stable: ${price}")

def vault_console():
    print("=== 🔐 ChronoDAO Vault Console v2.0 ===")
    vault = input("Enter your vault codename: ")
    scroll = input("Choose your scroll [1 = Summon Scrolls, 2 = ETH Watcher]: ")

    print(f"\n🧠 Welcome, {vault}.")

    if scroll == "1":
        for i in range(3):
            summon_scroll(f"Scroll-{i+1}", i+1)
    elif scroll == "2":
        prices = [3700, 3801, 3622, 3777]
        for p in prices:
            price_alert(p)
    else:
        print("❌ Unknown ritual. Please return with the correct spell.")

    print("⚙️ Protocol Complete.\n")

vault_console()
