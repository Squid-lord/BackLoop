import os
import json
import time

CONFIG_PATH = "src/config.json"

def load_config():
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ Config file not found. Please make sure src/config.json exists.")
        return {}

def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

def toggle_backloop():
    while True:
        print("\n=== 🔁 Backloop Control Panel ===")
        print("1️⃣  Turn ON Backloop")
        print("2️⃣  Turn OFF Backloop")
        print("3️⃣  View Configuration")
        print("4️⃣  Exit")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            print("🚀 Launching Backloop detector in background...")
            os.system("nohup python src/detector.py &")
            print("✅ Backloop is now running silently.")
        
        elif choice == "2":
            print("🛑 Stopping Backloop detector...")
            os.system("pkill -f detector.py")
            print("✅ Backloop stopped.")
        
        elif choice == "3":
            config = load_config()
            print("\n📄 Current Configuration:")
            print(json.dumps(config, indent=4))
        
        elif choice == "4":
            print("👋 Exiting Backloop. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    toggle_backloop()
