import random

def process_payment(amount):
    print(f"Processing payment of ₹{amount}...")
    if random.choice([True, False]):
        print("Payment Successful!")
        return True
    else:
        print("Payment Failed! Please try again.")
        return False
