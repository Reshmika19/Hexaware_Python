import inspect
from productCatalog import ProductCatalogDB

def test_add_category_query():
    db = ProductCatalogDB()
    expected_query = "INSERT INTO categories (category_name) VALUES (%s)"
    actual_query = inspect.getsource(db.add_category)
    assert expected_query in actual_query

def test_add_product_query():
    db = ProductCatalogDB()
    expected_query = "INSERT INTO products (name, category_id, price, stock_quantity) VALUES (%s, %s, %s, %s)"
    actual_query = inspect.getsource(db.add_product)
    assert expected_query in actual_query

def test_update_product_query():
    db = ProductCatalogDB()
    expected_query = "UPDATE products SET price = %s WHERE product_id = %s"
    actual_query = inspect.getsource(db.update_product)
    assert expected_query in actual_query

def test_delete_product_query():
    db = ProductCatalogDB()
    expected_query = "DELETE FROM products WHERE product_id = %s"
    actual_query = inspect.getsource(db.delete_product)
    assert expected_query in actual_query

def test_search_products_query():
    db = ProductCatalogDB()
    expected_query = "SELECT * FROM products WHERE 1=1"
    actual_query = inspect.getsource(db.search_products)
    assert expected_query in actual_query

def test_low_stock_report_query():
    db = ProductCatalogDB()
    expected_query = "SELECT * FROM products WHERE stock_quantity < %s"
    actual_query = inspect.getsource(db.low_stock_report)
    assert expected_query in actual_query

def test_display_products_with_categories_query():
    db = ProductCatalogDB()
    expected_query = "SELECT p.product_id, p.name, c.category_name, p.price, p.stock_quantity"
    actual_query = inspect.getsource(db.display_products_with_categories)
    assert expected_query in actual_query
