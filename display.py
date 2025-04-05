# display.py
import json
def get_customer_data(name):
    with open("customer_data.json") as f:
        data = json.load(f)
    return data.get(name, {})
