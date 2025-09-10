from order import Order

class User:
    def __init__(self, name):
        self.name = name
        self.order = Order(self)

    def calculate_total(self):
        return self.order.calculate_total()

    
class PremiumUser(User):
    def calculate_total(self):
        total = super().calculate_total()
        return total * 0.85  
