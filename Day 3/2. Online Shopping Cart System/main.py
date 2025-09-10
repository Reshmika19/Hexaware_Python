'''
Case Study 2: Online Shopping Cart System
Problem Statement:
Design a shopping cart system for an online store that allows users to add products, remove
products, and calculate the total cost.
'''
from product import Product
from user import User, PremiumUser

# Create products
laptop = Product("Laptop", 1000, 5)
mouse = Product("Mouse", 50, 10)
keyboard = Product("Keyboard", 100, 7)

# Alice
alice = User("Alice")
alice.cart.add_product(laptop, 1)
alice.cart.add_product(mouse, 2)
alice.cart.remove_product(mouse, 1)
alice.cart.view_cart()
alice.calculate_total()

# Bob
bob = PremiumUser("Bob")
bob.cart.add_product(laptop, 2)
bob.cart.add_product(keyboard, 1)
bob.cart.view_cart()
bob.calculate_total()
