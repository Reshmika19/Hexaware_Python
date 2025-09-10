from product import Product

class Cart:
    def __init__(self, owner):
        self.owner = owner     
        self.items = {}
        self.last_added_item = None

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            product.stock -= quantity
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            self.last_added_item = product.name
            print(f"Added '{product.name}' to {self.owner.name}'s cart.")
        else:
            print(f"Not enough stock for {product.name}.")

    def remove_product(self, product, quantity):
        if product in self.items:
            if quantity >= self.items[product]:
                product.stock += self.items[product]
                print(f"Removed '{product.name}' from {self.owner.name}'s cart.")
                del self.items[product]
            else:
                self.items[product] -= quantity
                product.stock += quantity
                print(f"Removed {quantity} of '{product.name}' from {self.owner.name}'s cart.")
        else:
            print(f"{product.name} not found in {self.owner.name}'s cart.")

    def view_cart(self):
        if not self.items:
            print(f"{self.owner.name}'s cart is empty.")
        else:
            print(f"{self.owner.name}'s cart items:")
            for product, qty in self.items.items():
                print(f"- {product.name} (x{qty}) - ${product.price * qty}")

    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.items.items())
