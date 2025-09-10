class FoodItem:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

    def display(self):
        status = "Available" if self.available else "Not Available"
        print(f"{self.name} - ${self.price} ({status})")
