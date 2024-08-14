
# example_usage.py

from ecommerce.products.product_management import Product, add_product, remove_product
from ecommerce.products.inventory import check_inventory
from ecommerce.orders.order_processing import Order, create_order, get_order

def main():
    product_list = []
    order_list = []

    # Add products
    product1 = Product(1, "Laptop", 1500)
    product2 = Product(2, "Smartphone", 800)
    add_product(product_list, product1)
    add_product(product_list, product2)

    print("Products:", product_list)

    # Check inventory
    product = check_inventory(product_list, 1)
    print("Inventory check for product ID 1:", product)

    # Create an order
    order1 = Order(1, [product1, product2])
    create_order(order_list, order1)

    print("Orders:", order_list)

    # Get an order
    order = get_order(order_list, 1)
    print("Order with ID 1:", order)

if __name__ == "__main__":
    main()

