# main.py — Backloop main controller with memory
import json
import os
from utils import toggle_backloop

CONFIG_PATH = "src/config.json"

def load_config():
    if not os.path.exists(CONFIG_PATH):
        default = {"reel_blocker": False, "auto_return_time": 3, "allowed_apps": ["WhatsApp", "YouTube"]}
        save_config(default)
        return default
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

def auto_start():
    config = load_config()
    if config.get("reel_blocker"):
        toggle_backloop(True)
        print("⚙️ Auto-start: Backloop is ON (from last session).")
    else:
        print("⚙️ Auto-start: Backloop is OFF (from last session).")

def show_menu():
    print("\n--- Backloop Control Menu ---")
    print("1. Turn ON Backloop")
    print("2. Turn OFF Backloop")
    print("3. Show Current Status")
    print("4. Exit")
    print("------------------------------")

def main():
    auto_start()  # <-- This line loads previous state automatically
    while True:
        show_menu()
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            config = load_config()
            config["reel_blocker"] = True
            save_config(config)
            toggle_backloop(True)
            print("✅ Backloop is now ON.\n")

        elif choice == "2":
            config = load_config()
            config["reel_blocker"] = False
            save_config(config)
            toggle_backloop(False)
            print("❌ Backloop is now OFF.\n")

        elif choice == "3":
            config = load_config()
            status = "ON" if config["reel_blocker"] else "OFF"
            print(f"📊 Current Status: Backloop is {status}")
            print(f"Auto Return Time: {config['auto_return_time']} sec")
            print(f"Allowed Apps: {', '.join(config['allowed_apps'])}\n")

        elif choice == "4":
            print("👋 Exiting Backloop. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
