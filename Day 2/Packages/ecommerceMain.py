# 2. ecommerce Package (cart.py, payment.py)
'''
An online shopping platform needs to manage carts and payments.
• cart.py → Add items, remove items, calculate total.
• payment.py → Simulate payment (success/failure).
'''

from ecommerce import add_item, remove_item, calculate_total, show_cart, process_payment

def main():
    # Add items
    add_item("Laptop", 50000, 1)
    add_item("Mouse", 1000, 2)
    add_item("Keyboard", 2000, 1)

    print("\nYour Cart:")
    show_cart()

    # Remove example
    remove_item("Mouse")

    print("\nUpdated Cart:")
    show_cart()

    # Calculate total
    total = calculate_total()
    print(f"\nTotal Bill: ₹{total}")

    # Process payment
    process_payment(total)

if __name__ == "__main__":
    main()
