import tkinter as tk
from modules.mm import purchase
from modules.sd import sell
from modules.fi import get_balance

def start_app():
    root = tk.Tk()
    root.title("SAP Simulation System")

    def buy():
        mat = entry_material.get()
        qty = int(entry_qty.get())
        result.set(purchase(mat, qty))

    def sell_item():
        mat = entry_material.get()
        qty = int(entry_qty.get())
        price = int(entry_price.get())
        result.set(sell(mat, qty, price))

    def show_balance():
        result.set(f"Balance: ₹{get_balance()}")

    tk.Label(root, text="Material").pack()
    entry_material = tk.Entry(root)
    entry_material.pack()

    tk.Label(root, text="Quantity").pack()
    entry_qty = tk.Entry(root)
    entry_qty.pack()

    tk.Label(root, text="Price").pack()
    entry_price = tk.Entry(root)
    entry_price.pack()

    result = tk.StringVar()

    tk.Button(root, text="Purchase (MM)", command=buy).pack()
    tk.Button(root, text="Sell (SD)", command=sell_item).pack()
    tk.Button(root, text="Check Balance (FI)", command=show_balance).pack()

    tk.Label(root, textvariable=result).pack()

    root.mainloop()