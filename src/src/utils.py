# utils.py
# Helper functions for Backloop
def toggle_backloop(state):
    """
    Simulates turning Backloop on or off.
    """
    if state:
        return "Backloop activated."
    else:
        return "Backloop deactivated."
