# utils.py — helper functions for Backloop

def toggle_backloop(state):
    if state:
        print("🔄 Backloop system activated.")
        print("Reel blocker will auto-return from shorts/reels.")
    else:
        print("⏹ Backloop system deactivated.")
        print("You can now use all apps freely.")
