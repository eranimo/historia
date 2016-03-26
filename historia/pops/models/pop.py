from historia.utils import unique_id


class Pop(object):
    """
    A simulated unit of population
    """

    def __init__(self, province, pop_type, population):
        """
        Creates a new Pop.
        manager  (Historia)
        province (SecondaryDivision)
        culture  (Culture)
        religion (Religion)
        language (Language)
        job      (Job)
        """
        self.province = province
        self.id = unique_id('po')

        self.population = population

        self.pop_type = pop_type
        self.savings = 0

        # ECONOMY
        self.inventory = [] # List of Good, int tuples
        self.money = 0 # current wealth of Pop
        self.bankrupt = False # set when bankrupcy conditions are met
        self.price_belief = {} # a map of resources to PriceRange instances
        self.visiting = None # if the pop is visiting another Market to trade

        self.owned_rgos = [] # a list of RGOs that this pop owns
        self.employer_rgo = None # which RGO this pop is employed at

        self.province.manager.logger.log(self, {
            'pop_type': self.pop_type.ref(),
            'province': province.id
        })


    # Economic methods
    @property
    def market(self):
        return self.province.market

    def perform_production(self):
        "Depending on PopType, perform production by reducing inventory and producing another item"
        pass

    def generate_offers(self):
        """
        If the Pop needs a Good to perform production, buy it
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

    def export(self):
        return {
            'pop_type': self.pop_type.ref()
        }
