"""
solid is a abbreviation stands for five design principles.
- single responsibility
- open-closed principle
- liskov substitute
- interface seggregation
- dependency inversion
"""


#  single responsibility
#  A class or a method should have only one job or one reason to change


class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Order:
    def __init__(self, order_id, item):
        self.order_id = (order_id,)
        self.item = item


# adding payment method


class Payment:
    def debit_pay(self, order):
        print(f"processing payment for order id {order.order_id}")
        print("payment successfull")


item = [Item("phone", 2, 10000), Item("shirt", 2, 2000)]
order_obj = Order(order_id=1, item=item)

payment = Payment()
payment.debit_pay(order_obj)
