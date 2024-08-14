

# ecommerce/products/product_management.py

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.price})"

def add_product(product_list, product):
    product_list.append(product)

def remove_product(product_list, product_id):
    product_list[:] = [p for p in product_list if p.product_id != product_id]
