cart_items = {}  

def add_item(item, price, quantity=1):
    if item in cart_items:
        old_price, old_quantity = cart_items[item]
        cart_items[item] = (price, old_quantity + quantity)
    else:
        cart_items[item] = (price, quantity)

def remove_item(item):
    if item in cart_items:
        del cart_items[item]

def calculate_total():
    return sum(price * quantity for price, quantity in cart_items.values())

def show_cart():
    if not cart_items:
        print("Cart is empty.")
    else:
        for item, (price, qty) in cart_items.items():
            print(f"{item} - ₹{price} x {qty}")
