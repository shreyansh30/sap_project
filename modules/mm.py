inventory = {}

def purchase(material, qty):
    inventory[material] = inventory.get(material, 0) + qty
    return f"Purchased {qty} units of {material}"