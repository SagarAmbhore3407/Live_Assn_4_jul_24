

# ecommerce/orders/order_processing.py

class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products

    def __repr__(self):
        return f"Order({self.order_id}, {self.products})"

def create_order(order_list, order):
    order_list.append(order)

def get_order(order_list, order_id):
    for order in order_list:
        if order.order_id == order_id:
            return order
    return None
