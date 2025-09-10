'''
4. Online Food Delivery System

Problem Statement:
Design an online food delivery system that allows users to browse restaurants, add food items to an
order, and place the order with optional discounts for premium customers.
'''

from foodItem import FoodItem
from user import User, PremiumUser

biriyani = FoodItem("Biriyani", 500, available=True)
chicken = FoodItem("Chicken", 250, available=True)
parotta = FoodItem("Parotta", 150, available=False)

Resh = User("Resh")
Resh.order.add_item(biriyani)
Resh.order.add_item(chicken)
Resh.order.add_item(parotta)  
Resh.order.remove_item(parotta)
Resh.order.display_order()
print(f"{Resh.name}'s order total: Rs. {Resh.calculate_total()}\n")


Nila = PremiumUser("Nilla")
Nila.order.add_item(biriyani)
Nila.order.add_item(chicken)
Nila.order.display_order()
print(f"{Nila.name}'s order total with discount: Rs. {Nila.calculate_total()}")
