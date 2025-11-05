# detector.py — Simulated app detector for Backloop
import os
import time
import json

CONFIG_PATH = "src/config.json"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def detect_current_app():
    """Return the current foreground app’s package name."""
    try:
        output = os.popen("dumpsys activity activities | grep mResumedActivity").read()
        if "/" in output:
            pkg = output.split("/")[0].split()[-1]
            return pkg
        return "unknown"
    except Exception as e:
        return str(e)

def monitor_apps():
    """Continuously monitor and auto-return if blocked apps detected."""
    cfg = load_config()
    while cfg.get("reel_blocker", False):
        pkg = detect_current_app()
        if pkg not in ["com.whatsapp", "com.google.android.youtube", "com.android.launcher"]:
            print(f"⚠️ Detected blocked app: {pkg} → returning home!")
            os.system("input keyevent 3")  # simulate Home
        time.sleep(cfg.get("auto_return_time", 3))

if __name__ == "__main__":
    print("🔍 Monitoring apps... Press Ctrl+C to stop.")
    monitor_apps()
