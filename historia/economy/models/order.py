from uuid import uuid4
from historia.economy.enums.order_type import OrderType

class Order(object):
    """
    A class that represents a buy or sell order

    Properties:
    - pop (Pop)   The pop who made this order
    - order_type (OrderType)  The type of order this is
    - resource (ResourceType) What resource this order is for
    - quantity (float)    The amount of Good this order is for
    - price (float)   How much the order is
    """

    def __init__(self, pop, order_type, quantity, price, resource):
        self.pop = pop
        self.order_type = order_type
        self.quantity = quantity
        self.price = price
        self.resource = resource
        self.id = uuid4().hex

    def __str__(self):
        """ Formatting for console printing """
        return "[] ({}) {}: {:,} @ ${:,.2}".format(self.order_type,
                                                   self.pop.id,
                                                   self.resource.resource_type,
                                                   self.resource.amount,
                                                   self.price)
