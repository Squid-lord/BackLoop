import time, json, os

CONFIG_PATH = "src/config.json"

def get_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def get_current_app():
    # This example assumes Android `dumpsys` is used for foreground detection
    try:
        app = os.popen("dumpsys window | grep mCurrentFocus").read()
        return app
    except:
        return None

def detector_loop():
    config = get_config()
    targets = config["allowed_apps"]
    wait = config["auto_return_time"]

    print("👁️ Backloop Detector active.")
    while True:
        app = get_current_app()
        if any(pkg in str(app) for pkg in targets):
            print(f"⚠️ Detected {app.strip()} — returning to home screen in {wait}s.")
            time.sleep(wait)
            os.system("input keyevent 3")  # Press HOME
        time.sleep(1)

if __name__ == "__main__":
    detector_loop()
