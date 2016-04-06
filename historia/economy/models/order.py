from uuid import uuid4
from historia.economy.enums.order_type import OrderType

class Order(object):
    """
    A class that represents a buy or sell order

    Properties:
    - pop (Pop)   The pop who made this order
    - order_type (OrderType)  The type of order this is
    - good (ResourceType) What good this order is for
    - quantity (float)    The amount of Good this order is for
    - price (float)   How much the order is
    """

    def __init__(self, pop, order_type, quantity, price, good):
        self.pop = pop
        self.order_type = order_type
        self.quantity = quantity
        self.price = price
        self.good = good
        self.id = uuid4().hex

    def __repr__(self):
        "Formatting for console printing"
        str_r = "<Order ({}) {}: {} @ ${:,}>"
        return str_r.format(self.order_type.name, self.good.name, self.quantity, self.price)

    def export(self):
        "Export as dict"
        return {
            'id': self.id,
            'pop': self.pop.id,
            'order_type': self.order_type.ref(),
            'quantity': self.quantity,
            'price': self.price,
            'good': self.good.ref()
        }
