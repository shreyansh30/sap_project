from modules.mm import inventory
from modules.fi import revenue

def sell(product, qty, price):
    if inventory.get(product, 0) >= qty:
        inventory[product] -= qty
        revenue(qty * price)
        return f"Sold {qty} units of {product}"
    else:
        return "Not enough stock"