from config import get_connection
from mysql.connector import Error

class ProductCatalogDB:
    
    def add_category(self, category_name):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO categories (category_name) VALUES (%s)",
                (category_name,)
            )
            conn.commit()
            print(f"Category '{category_name}' added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def add_product(self, name, category_id, price, stock_quantity):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO products (name, category_id, price, stock_quantity) VALUES (%s, %s, %s, %s)",
                (name, category_id, price, stock_quantity)
            )
            conn.commit()
            print(f"Product '{name}' added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def update_product(self, product_id, price=None, stock_quantity=None):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            if price is not None:
                cursor.execute(
                    "UPDATE products SET price = %s WHERE product_id = %s",
                    (price, product_id)
                )
            if stock_quantity is not None:
                cursor.execute(
                    "UPDATE products SET stock_quantity = %s WHERE product_id = %s",
                    (stock_quantity, product_id)
                )
            conn.commit()
            print(f"Product {product_id} updated successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def delete_product(self, product_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
            conn.commit()
            print(f"Product {product_id} deleted successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def search_products(self, name=None, category_id=None, min_price=None, max_price=None):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM products WHERE 1=1"
            params = []
            if name:
                query += " AND name LIKE %s"
                params.append(f"%{name}%")
            if category_id:
                query += " AND category_id = %s"
                params.append(category_id)
            if min_price is not None and max_price is not None:
                query += " AND price BETWEEN %s AND %s"
                params.extend([min_price, max_price])
            cursor.execute(query, tuple(params))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def low_stock_report(self, threshold):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE stock_quantity < %s", (threshold,))
            rows = cursor.fetchall()
            print("Low Stock Report:")
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def display_products_with_categories(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.product_id, p.name, c.category_name, p.price, p.stock_quantity
                FROM products p
                JOIN categories c ON p.category_id = c.category_id
            """)
            rows = cursor.fetchall()
            print("Products with Categories:")
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
