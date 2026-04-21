balance = 0

def expense(amount):
    global balance
    balance -= amount

def revenue(amount):
    global balance
    balance += amount

def get_balance():
    return balance