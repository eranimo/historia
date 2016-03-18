from uuid import uuid4

class Pop(object):
    """
    A simulated unit of population
    """

    def __init__(self, location, pop_type, population):
        """
        Creates a new Pop.
        manager  (Historia)
        location (SecondaryDivision)
        culture  (Culture)
        religion (Religion)
        language (Language)
        job      (Job)
        """
        self.location = location
        self.id = uuid4().hex

        self.population = population

        self.pop_type = pop_type
        self.savings = 0

        # ECONOMY
        self.inventory = [] # List of Resource, int tuples
        self.money = 0 # current wealth of Pop
        self.bankrupt = False # set when bankrupcy conditions are met
        self.price_belief = {} # a map of resources to PriceRange instances
        self.visiting = None # if the pop is visiting another Market to trade

        self.owned_rgos = [] # a list of RGOs that this pop owns
        self.employer_rgo = None # which RGO this pop is employed at


    # Economic methods
    @property
    def market(self):
        return self.location.market

    def perform_production(self):
        "Depending on PopType, perform production by reducing inventory and producing another item"
        pass

    def generate_offers(self):
        """
        If the Pop needs a Resource to perform production, buy it
        If the Pop has surplus Resources, sell them
        """

    def update_price_model(self, order_type, resource, successful, price):
        "Update the Pop's price model for the given resource"
        pass

    def get_inventory(self, resource):
        try:
            return self.inventory.get(resource)
        except KeyError:
            self.inventory[resource] = 0
            return 0

    def change_inventory(self, resource, amount):
        try:
            self.inventory[resource] += amount
        except KeyError:
            self.inventory[resource] = amount

    def __repr__(self):
        return "<Pop: id={} type={}>".format(self.id, self.pop_type.title)

    def __eq__(self, other):
        return self.id == other.id

    def __key__(self):
        return self.id

    def __hash__(self):
        return hash(self.__key__())
