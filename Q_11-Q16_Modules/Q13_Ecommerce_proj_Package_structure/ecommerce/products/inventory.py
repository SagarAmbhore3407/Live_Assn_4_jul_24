

# ecommerce/products/inventory.py

def check_inventory(product_list, product_id):
    for product in product_list:
        if product.product_id == product_id:
            return product
    return None
