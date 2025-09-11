from productCatalog import ProductCatalogDB

db = ProductCatalogDB()

def menu():
    while True:
        print("\n---------- Product Catalog Menu --------")
        print("1. Add Category")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Products")
        print("6. Low Stock Report")
        print("7. Display Products with Categories")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            name = input("Enter category name: ")
            db.add_category(name)

        elif choice == '2':
            name = input("Enter product name: ")
            category_id = int(input("Enter category ID: "))
            price = float(input("Enter price: "))
            stock = int(input("Enter stock quantity: "))
            db.add_product(name, category_id, price, stock)

        elif choice == '3':
            product_id = int(input("Enter product ID to update: "))
            price_input = input("Enter new price (leave blank to skip): ")
            stock_input = input("Enter new stock quantity (leave blank to skip): ")
            price = float(price_input) if price_input else None
            stock = int(stock_input) if stock_input else None
            db.update_product(product_id, price, stock)

        elif choice == '4':
            product_id = int(input("Enter product ID to delete: "))
            db.delete_product(product_id)

        elif choice == '5':
            name = input("Search by name (leave blank to skip): ")
            category_id_input = input("Search by category ID (leave blank to skip): ")
            min_price_input = input("Min price (leave blank to skip): ")
            max_price_input = input("Max price (leave blank to skip): ")

            category_id = int(category_id_input) if category_id_input else None
            min_price = float(min_price_input) if min_price_input else None
            max_price = float(max_price_input) if max_price_input else None

            db.search_products(name, category_id, min_price, max_price)

        elif choice == '6':
            threshold = int(input("Enter stock threshold: "))
            db.low_stock_report(threshold)

        elif choice == '7':
            db.display_products_with_categories()

        elif choice == '8':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
