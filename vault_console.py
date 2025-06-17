def launch_console():
    print("=== 🔐 Vault Console v0.1 ===")
    name = input("Enter your vault codename: ")
    ritual = input("What scroll do you wish to summon? ")

    print(f"\n🧠 Welcome, {name}.")
    print(f"📜 Scroll '{ritual}' has been summoned and sealed.")

    # Moved inside the function:
    if ritual == "Founder Fire":
        print("🔥 Initiating genesis airdrop...")
    elif ritual == "Codex":
        print("📖 Displaying all vault protocols...")
    else:
        print("❌ Unknown scroll. Access denied.")

    print("⚙️ Protocol complete.")

# Run the ritual
launch_console()
