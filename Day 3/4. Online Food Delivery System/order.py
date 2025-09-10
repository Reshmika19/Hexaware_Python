from foodItem import FoodItem

class Order:
    def __init__(self, user):
        self.user = user
        self.items = []
        self.last_ordered_item = None  

    def add_item(self, food_item):
        if food_item.available:
            self.items.append(food_item)
            self.last_ordered_item = food_item.name
            print(f"Added '{food_item.name}' to {self.user.name}'s order.")
        else:
            print(f"Sorry, {food_item.name} is not available.")

    def remove_item(self, food_item):
        if food_item in self.items:
            self.items.remove(food_item)
            print(f"Removed '{food_item.name}' from {self.user.name}'s order.")
        else:
            print(f"{food_item.name} is not in {self.user.name}'s order.")

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def display_order(self):
        print(f"{self.user.name}'s order:")
        if not self.items:
            print("No items in order.")
        else:
            for item in self.items:
                print(f"- {item.name} - ${item.price}")

