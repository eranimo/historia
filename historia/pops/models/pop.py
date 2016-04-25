import math
from historia.utils import unique_id, position_in_range
from historia.pops.models.inventory import Inventory
from historia.economy.enums.resource import Good
from historia.economy.enums.order_type import OrderType
from historia.economy.models.price_range import PriceRange
from historia.economy.models.order import Order

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
        self.bankrupt_times = 0
        self.province = province
        self.id = unique_id('po')

        self.population = population
        self.population_yesterday = 0

        self.pop_type = pop_type

        # ECONOMY
        self.money = 10
        self.money_yesterday = 0
        self.bankrupt = False

        # set inventory and ideal amounts
        self.inventory = Inventory(150)
        for item in self.pop_type.start_inventory:
            self.inventory.add(item['good'], item['amount'])

        self.update_ideal_inventory()

        # a dictionary of Goods to PriceRanges
        # represents the price range the agent considers valid for each Good
        self.price_belief = {}

        # a dictionary of Goods to price list
        # represents the prices of the good that the Pop has observed
        # during the time they have been trading
        self.observed_trading_range = {}

        self.successful_trades = 0
        self.failed_trades = 0


        # make some fake initial data
        for good in Good.all():
            avg_price = self.market.avg_historial_price(good, 15)
            # fake trades
            self.observed_trading_range[good] = [
                avg_price * 0.5,
                avg_price * 1.5
            ]
            # generate fake price belief
            self.price_belief[good] = PriceRange(avg_price * 0.5, avg_price * 1.5)

    def update_ideal_inventory(self):
        "Update ideal inventory"
        for item in self.pop_type.ideal_inventory:
            self.inventory.set_ideal(item['good'], item['amount'])

    def change_population(self, trade_success):
        "Change the population based off the trade"
        self.population_yesterday = self.population
        if trade_success:
            self.population += round(self.population * 0.002)
        else:
            self.population -= round(self.population * 0.002)


    def handle_bankruptcy(self, pop_type):
        "Change job, create money out of thin air, update ideal inventory"
        self.pop_type = pop_type
        self.bankrupt_times += 1
        self.money = 2
        self.update_ideal_inventory()


    # Economic methods
    @property
    def market(self):
        "Get the market instance"
        return self.province.market

    @property
    def profit(self):
        "Determine profit"
        return self.money - self.money_yesterday

    def perform_production(self):
        "Depending on PopType, perform production by reducing inventory and producing another item"
        logic = self.pop_type.logic(self)
        logic.perform()

    def create_buy_order(self, good, limit):
        "Create a buy order for a given Good at a determined quantity"
        bid_price = self.determine_price_of(good)
        ideal = self.determine_buy_quantity(good)

        # can't buy more than limit
        quantity_to_buy = limit if ideal > limit else ideal
        if quantity_to_buy > 0:
            return Order(self, OrderType.buy_order, quantity_to_buy, bid_price, good)
        return False

    def create_sell_order(self, good, limit):
        "Create a sell order for a given Good at a determined quantity"
        sell_price = self.determine_price_of(good)
        ideal = self.determine_sell_quantity(good)

        # can't buy more than limit
        quantity_to_sell = limit if ideal < limit else ideal
        if quantity_to_sell > 0:
            return Order(self, OrderType.sell_order, quantity_to_sell, sell_price, good)
        return False

    def price_belief_for(self, good):
        "Gets the price belief this agent has for a particular Good"
        if good in self.price_belief:
            return self.price_belief[good]

    def determine_price_of(self, good):
        "Determine the price of a particular good"
        return self.price_belief_for(good).random()

    def trading_range_extremes(self, good):
        "Gets the lowest and highst price of a Good this agent has seen"
        trading_range = self.observed_trading_range[good]
        return PriceRange(min(trading_range), max(trading_range))

    def determine_sell_quantity(self, good):
        "Determine how much inventory goods to sell based on market conditions"
        mean = self.market.avg_historial_price(good, 15)
        trading_range = self.trading_range_extremes(good)

        favoribility = position_in_range(mean, trading_range.low, trading_range.high)
        amount_to_sell = round(favoribility * self.inventory.surplus(good))
        if amount_to_sell < 1:
            amount_to_sell = 1
        return amount_to_sell

    def determine_buy_quantity(self, good):
        "Determine how much goods to buy based on market conditions"
        mean = self.market.avg_historial_price(good, 15)
        trading_range = self.trading_range_extremes(good)

        favoribility = 1 - position_in_range(mean, trading_range.low, trading_range.high)
        amount_to_buy = round(favoribility * self.inventory.shortage(good))
        if amount_to_buy < 1:
            amount_to_buy = 1
        return amount_to_buy

    def generate_orders(self, good):
        """
        If the Pop needs a Good to perform production, buy it
        If the Pop has surplus Resources, sell them
        """
        surplus = self.inventory.surplus(good)
        if surplus >= 1: # sell inventory
            # the original only old one item here
            sell_amount = surplus
            order = self.create_sell_order(good, surplus)
            if order:
                # print('{} sells {} {}'.format(self.pop_type.title, sell_amount, good.name))
                self.market.sell(order)
        else: # buy more
            shortage = self.inventory.shortage(good)
            free_space = self.inventory.empty_space

            if shortage > 0:
                if shortage <= free_space:
                    # enough space for ideal order
                    limit = shortage
                else:
                    # not enough space for ideal order
                    limit = math.floor(free_space / shortage)

                if limit > 0:
                    order = self.create_buy_order(good, limit)
                    if order:
                        # print('{} buys {} {}'.format(self.pop_type.title, limit, good.name))
                        self.market.buy(order)
            # else:
            #     print("{} has no shortage of {} (has shortage: {})".format(self.pop_type.title, good.title, shortage))



    def update_price_model(self, good, order_type, is_successful, clearing_price=0):
        """
        Update the Pop's price model for the given resource
        good (Good)             The Good which was orderd
        order_type (OrderType)  Which kind of Order this was
        is_successful (bool)    whether or not the Order was successful
        clearing_price (float)  The price per unit of the good that was ordered
                                as defined by the Pop which ordered it
        """

        SIGNIFICANT = 0.25 # 25% more or less is "significant"
        SIG_IMBALANCE = 0.33
        LOW_INVENTORY = 0.1 # 10% of ideal inventory = "LOW"
        HIGH_INVENTORY = 2.0 # 200% of ideal inventory = "HIGH"
        MIN_PRICE = 0.01 # lowest allowed price of a Good

        if is_successful:
            # add this trade to the observed trading range
            self.observed_trading_range[good].append(clearing_price)

        public_mean_price = self.market.avg_historial_price(good, 1)
        belief = self.price_belief[good]
        mean = belief.mean()
        wobble = 0.05 # the degree which the Pop should bid outside the belief

        # how different the public mean price is from the price belief
        delta_to_mean = mean - public_mean_price

        if is_successful:
            if order_type is OrderType.buy_order and delta_to_mean > SIGNIFICANT:
                # this Pop overpaid, shift belief towards mean
                belief.low -= delta_to_mean / 2
                belief.high -= delta_to_mean / 2
            elif order_type is OrderType.sell_order and delta_to_mean < -SIGNIFICANT:
                # this Pop underpaid!, shift belief towards mean
                belief.low -= delta_to_mean / 2
                belief.high -= delta_to_mean / 2

            # increase the belief's certainty
            belief.low += wobble * mean
            belief.high -= wobble * mean

        else:
            # shift towards mean
            belief.low -= delta_to_mean / 2
            belief.high -= delta_to_mean / 2

            # check for inventory special cases
            stocks = self.inventory.get_amount(good)
            ideal = self.inventory.get_ideal(good)

            # if we're buying and inventory is too low
            # meaning we're desperate to buy
            if order_type is OrderType.buy_order and stocks < LOW_INVENTORY * ideal:
                wobble *= 2

            # if we're selling and inventory is too high
            # meaning we're desperate to sell
            elif order_type is OrderType.sell_order and stocks > HIGH_INVENTORY * ideal:
                wobble *= 2
            # all other cases
            else:
                sells = self.market.history.sell_orders.average(good, 1)
                buys = self.market.history.buy_orders.average(good, 1)

                # TODO: figure out why this is sometimes 0
                if sells + buys > 0:

                    supply_vs_demand = (sells - buys) / (sells + buys)

                    if supply_vs_demand > SIG_IMBALANCE or supply_vs_demand < -SIG_IMBALANCE:
                        # too much supply? lower bid lower to sell faster
                        # too much demand? raise price to buy faster

                        new_mean = public_mean_price * (1 - supply_vs_demand)
                        delta_to_mean = mean - new_mean

                        # shift the price belief to the new price mean
                        belief.low -= delta_to_mean / 2
                        belief.high -= delta_to_mean / 2


            # decrease belief's certainty since we've just changed it (we could be wrong)
            belief.low -= wobble * mean
            belief.high += wobble * mean

        # make sure the price belief doesn't decrease below the minimum
        if belief.low < MIN_PRICE:
            belief.low = MIN_PRICE
        elif belief.high < MIN_PRICE:
            belief.high = MIN_PRICE

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
            'pop_type': self.pop_type.ref(),
            'population': self.population,
            'population_yesterday': self.population_yesterday,
            'inventory': self.inventory.export(),
            'money': self.money,
            'money_yesterday': self.money_yesterday,
            'successful_trades': self.successful_trades,
            'failed_trades': self.failed_trades,
            'bankrupt_times': self.bankrupt_times,
        }
