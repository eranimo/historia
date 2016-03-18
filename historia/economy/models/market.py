from historia.economy.models.order import Order

class Market(object):
    """
    A class that handles and stores market buy and sell orders from pops.
    A second-level division has an instance of a Market class.

    Parameters:
    manager Historia
    location SecondaryDivision

    Properties:
    buy_orders list[Order]
    sell_orders list[Order]

    order_history
    """

    def __init__(self, manager, location):
        self.manager = manager
        self.location = location

        self.buy_orders = []
        self.sell_orders = []

    def resolve_orders(self):
        """
        Fufill all orders that can be resolved
        """
        pass

    def price_of(self, resource):
        "Determines the price of a given resource at this Market"
        pass

    def average_historial_price(self, resource, range):
        "Gets the average historical price of a resource *range* years back"
        pass

    def simulate(self):
        "Simulate a round of trading between the agents at this Market"
        for pop in self.location.pops:
            pop.perform_production()
            pop.generate_offers()
        # resolve all offers for each Resource
        for pop in self.location.pops:
            if pop.money < 0:
                pop.bankrupt = True

    def create_sell_order(self, pop, resource, limit):
        pass

    def create_buy_order(self, pop, resource, limit):
        pass

    def resolve_offers():
        pass
