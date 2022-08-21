import json

def LoadOrders():
    file_path = 'settings\orders.json'
    first = 'user_orders'
    second = 'orders'

    with open(file_path) as f:
        data = json.load(f)

    for state in data[first]:
        loaded_data = state[second]

    return loaded_data