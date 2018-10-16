"""
Let's assume we don't want to run under 15% of the battery capacity
"""

def get_usable_battery(amps):
    return float(amps) * 1.15
