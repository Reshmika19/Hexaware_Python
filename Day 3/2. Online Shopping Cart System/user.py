from cart import Cart

class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart(self)   

    def calculate_total(self):
        total = self.cart.calculate_total()
        print(f"{self.name}'s cart total: ${total}")
        return total


class PremiumUser(User):
    def calculate_total(self):
        total = self.cart.calculate_total()
        discount = total * 0.10
        total_after_discount = total - discount
        print(f"{self.name}'s cart total with discount: ${total_after_discount}")
        return total_after_discount
