# main.py
# Backloop main controller

import json
from utils import toggle_backloop

# Load settings from config.json
def load_config():
    with open("src/config.json", "r") as file:
        return json.load(file)

# Save settings to config.json
def save_config(config):
    with open("src/config.json", "w") as file:
        json.dump(config, file, indent=4)

# Main program simulation
def run_backloop():
    config = load_config()
    if config["backloop_enabled"]:
        print("Backloop is running...")
        print(toggle_backloop(True))
    else:
        print("Backloop is off.")
        print(toggle_backloop(False))

if __name__ == "__main__":
    run_backloop()
