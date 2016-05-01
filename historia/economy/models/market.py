from random import shuffle
from itertools import groupby
from operator import itemgetter

from historia.economy.models.order import Order
from historia.economy.enums.order_type import OrderType
from historia.economy.enums.resource import Good
from historia.pops.enums.pop_job import PopJob, JOBS_CLASS

from historia.economy.models.trade_history import TradeHistory, TradeHistoryLog

GOOD_POPJOB_MAP = {
    Good.grain: PopJob.farmer,
    Good.iron_ore: PopJob.miner,
    Good.lumber: PopJob.miller,
    Good.timber: PopJob.woodcutter,
    Good.tools: PopJob.blacksmith,
    Good.iron: PopJob.refiner,
    Good.bread: PopJob.baker
}

DEBUG = False

class Market:
    """
    A class that handles and stores market buy and sell orders from pops.
    A second-level division has an instance of a Market class.

    Parameters:
    manager Historia
    location Province

    Properties:
    buy_orders list[Order]
    sell_orders list[Order]

    history TradeHistory
    """

    def __init__(self, manager, location):
        self.manager = manager
        self.location = location

        # dictionary of list of orders by Good
        # stores the current buy and sell orders this market is processing
        self.buy_orders = {}
        self.sell_orders = {}

        # stores historical economic data for past transactions
        self.history = TradeHistory()

        # fill the trade history with a bunch of fake data
        for good in Good.all():
            self.history.register(good)
            self.history.prices.add(good, 1.0)
            self.history.buy_orders.add(good, 1.0)
            self.history.sell_orders.add(good, 1.0)
            self.history.trades.add(good, 1.0)
            self.buy_orders[good] = []
            self.sell_orders[good] = []

        for pop_job in PopJob.all():
            self.history.profit.register(pop_job)

    def __repr__(self):
        return "<Market location={}>".format(self.location.id)

    @property
    def pops(self):
        "Get all pops at this market"
        return self.location.pops

    def resolve_orders(self, good):
        "Fufill all orders that can be resolved for a particular Good"
        buy_orders = self.buy_orders[good]
        sell_orders = self.sell_orders[good]

        # shuffle all orders to remove bias
        shuffle(buy_orders)
        shuffle(sell_orders)

        # highest buy price first
        buy_orders.sort(key=lambda o: o.price, reverse=True)

        # lowest sell price first
        sell_orders.sort(key=lambda o: o.price, reverse=False)

        if DEBUG:
            if len(buy_orders) and len(sell_orders):
                print('Resolve Orders for {}'.format(good.title))
                print('\tBuy orders: {}'.format(len(buy_orders)))
                print('\tSell orders: {}'.format(len(sell_orders)))
            elif len(buy_orders) > len(sell_orders):
                print('Pops need to sell more {} (buys: {} sells: {})'.format(good.title, len(buy_orders), len(sell_orders)))
            elif len(buy_orders) < len(sell_orders):
                print('Pops need to buy more {} (buys: {} sells: {})'.format(good.title, len(buy_orders), len(sell_orders)))

        total_buy_amount = sum([o.quantity for o in buy_orders])
        total_sell_amount = sum([o.quantity for o in sell_orders])

        avg_price = 0 # avg clearing price this round
        units_traded = 0 # amount of goods traded this round
        money_traded = 0 # amount of money traded this round
        num_successful_trades = 0 # # of successful trades this round

        # match the highest buy orders to the lowest sell orders]
        while len(buy_orders) > 0 and len(sell_orders) > 0:
            buy_order = buy_orders[0]
            sell_order = sell_orders[0]
            if DEBUG:
                print('\t\tBuy:', buy_order)
                print('\t\tSell:', sell_order)

            # quantity traded. Defined as the mininum of both orders quantity
            # in the future this may be improved
            quantity_traded = min(buy_order.quantity, sell_order.quantity)

            # the price per unit. Defined as the average of both orders prices
            clearing_price = (buy_order.price + sell_order.price) / 2.0
            total_price = quantity_traded * clearing_price

            if DEBUG:
                print('\t\tPrice: {}'.format(total_price))

            if quantity_traded > 0:
                # trade the goods and money, recording this in the order
                sell_order.quantity -= quantity_traded
                buy_order.quantity -= quantity_traded

                self.transfer_good(good, quantity_traded, sell_order.pop, buy_order.pop, clearing_price)
                self.transfer_money(total_price, sell_order.pop, buy_order.pop)

                # handle taxes
                tax = total_price * self.location.owner.vat[good]
                buy_order.pop.money -= tax
                self.location.owner.money += tax

                # update Pop price beliefs due to successful trade
                buy_order.pop.update_price_model(good, OrderType.buy_order, True, clearing_price)
                sell_order.pop.update_price_model(good, OrderType.sell_order, True, clearing_price)

                # update pop metrics
                buy_order.pop.successful_trades += 1
                sell_order.pop.successful_trades += 1

                buy_order.pop.change_population(True)
                sell_order.pop.change_population(True)

                # log some stuff
                money_traded += total_price
                units_traded += quantity_traded
                num_successful_trades += 1

            # remove orders that have a quantity of 0
            if sell_order.quantity == 0:
                del sell_orders[0]

            if buy_order.quantity == 0:
                del buy_orders[0]

            if DEBUG:
                print('\n')

        # reject all orders which don't have a matching order
        while len(buy_orders) > 0:
            buy_orders[0].pop.update_price_model(good, OrderType.buy_order, False)
            # update pop metrics
            buy_orders[0].pop.failed_trades += 1
            buy_orders[0].pop.change_population(False)
            del buy_orders[0]

        while len(sell_orders) > 0:
            sell_orders[0].pop.update_price_model(good, OrderType.sell_order, False)
            # update pop metrics
            sell_orders[0].pop.failed_trades += 1
            sell_orders[0].pop.change_population(False)
            del sell_orders[0]

        # update history
        self.history.buy_orders.add(good, total_buy_amount)
        self.history.sell_orders.add(good, total_sell_amount)
        self.history.trades.add(good, units_traded)

        if units_traded > 0:
            self.history.prices.add(good, float(money_traded) / units_traded)
        else:
            # no units were traded this round, so use the last round's average price
            last_avg = self.history.prices.average(good, 1)
            self.history.prices.add(good, last_avg)

        pops = self.pops
        shuffle(pops)


        # pops grouped by pop_job
        # create a key in TradehistoryLog with a list of each agent's profit this round
        # grouped into their pop_job
        for pop_job, pops in groupby(self.pops, lambda x: x.pop_job):
            all_profits = [p.profit for p in pops]
            self.history.profit.extend(pop_job, all_profits)



    def buy(self, order):
        "Add a buy order Market"
        if order.order_type is OrderType.buy_order:
            self.buy_orders[order.good].append(order)
        else:
            raise Exception('Must be a buy order')

    def sell(self, order):
        "Add a sell order to the Market"
        if order.order_type is OrderType.sell_order:
            self.sell_orders[order.good].append(order)
        else:
            raise Exception('Must be a sell order')

    def decide_new_pop_job(self, pop):
        "Decide a new pop_job for a Pop when they go bankrupt"
        # include = JOBS_CLASS.get(pop.social_class)
        best_job = self.most_profitable_pop_job()
        best_good = self.most_demanded_good(day_range=3)
        if best_good is not None:
            best_job = GOOD_POPJOB_MAP[best_good]

        # if the best_job isn't valid at this location, and the best_good can be
        # found in neighboring provinces, become a merchant and import it

        if DEBUG:
            print("Pop {} ({}) is bankrupt. Switching to {}".format(pop.id, pop.pop_job.title, best_job.title))
        pop.handle_bankruptcy(best_job)

    def most_demanded_good(self, minimum=1.5, day_range=10):
        """
        Get the good with the highest demand/supply ratio over time
        minimum (float)     the minimum demand/supply ratio to consider an opportunity
        day_range (int)     number of rounds to look back
        """
        best_good = None
        best_ratio = float('-inf')
        for good in Good.all():
            sells = self.history.sell_orders.average(good, day_range=day_range)
            buys = self.history.buy_orders.average(good, day_range=day_range)

            if buys > 0 or sells > 0: # if this Good is traded in this Market

                if sells == 0 and buys > 0:
                    # make a fake supply of 0.5 for each unit to avoid
                    # an infinite ratio of supply to demand
                    sells = 0.5

                ratio = buys / sells

                if ratio > minimum and ratio > best_ratio:
                    best_ratio = ratio
                    best_good = good

        return best_good

    def goods_demand_ratio(self, day_range=10):
        """
        Get the good with the lowest demand/supply ratio over time
        day_range (int)     number of rounds to look back
        """
        demand_list = {}
        for good in Good.all():
            sells = self.history.sell_orders.average(good, day_range=day_range)
            buys = self.history.buy_orders.average(good, day_range=day_range)

            if buys > 0 or sells > 0: # if this Good is traded in this Market

                if sells == 0 and buys > 0:
                    # make a fake supply of 0.5 for each unit to avoid
                    # an infinite ratio of supply to demand
                    sells = 0.5

                ratio = buys / sells

                demand_list[good] = ratio
        return demand_list

    def most_cheap_good(self, day_range=10, exclude=None):
        """
        Returns the good that has the lowest average price over the given range of time
        range (int)           how many days to look back
        exclude (list[Good])  goods to exclude
        """
        best_good = None
        best_price = float('inf')

        for good in Good.all():
            if exclude is None or good not in exclude:
                price = self.mean_price(good)

                if price < best_price:
                    best_price = price
                    best_good = good

        return best_good

    def most_costly_good(self, day_range=10, exclude=None):
        """
        Returns the good that has the highest average price over the given range of time
        range (int)           how many days to look back
        exclude (list[Good])  goods to exclude
        """
        best_good = None
        best_price = float('inf')

        for good in Good.all():
            if exclude is None or good not in exclude:
                price = self.mean_price(good)

                if price > best_price:
                    best_price = price
                    best_good = good

        return best_good

    def most_profitable_pop_job(self, include=None, day_range=10):
        "Returns the most profitable pop_job in a given day range"
        best = float('-inf')
        best_pop_job = None

        if include is None:
            include = PopJob.all()

        for pop_job in include:
            avg_profit = self.history.profit.average(pop_job, day_range=day_range)

            if avg_profit > best:
                best_pop_job = pop_job
                best = avg_profit

        return best_pop_job

    def avg_historial_price(self, good, day_range):
        "Gets the average historical price of a resource *range* days back"
        return self.history.prices.average(good, day_range=day_range)

    def mean_price(self, good):
        "Get the mean price of a Good at this Market before today"
        return self.avg_historial_price(good, 1)

    def demand_for(self, good):
        "Get the number of buy orders for a good before today"
        return self.history.buy_orders.average(good, day_range=1)

    def supply_for(self, good):
        "Get the number of sell orders for a good before today"
        return self.history.sell_orders.average(good, day_range=1)

    def transfer_good(self, good, amount, seller, buyer, unit_price):
        "Transfers Goods from a seller Pop to a buyer Pop"
        seller.inventory.subtract(good, amount)
        buyer.inventory.add(good, amount, unit_price)

    def transfer_money(self, amount, seller, buyer):
        "Transfers money from a seller Pop to a buyer Pop"
        seller.money += amount
        buyer.money -= amount

    def simulate(self):
        "Simulate a round of trading between the agents(Pops) at this Market"
        pops_grouped = groupby(self.pops, lambda x: x.pop_job)
        # print(', '.join(["{}: {}".format(pop_job.title, len(list(pops))) for pop_job, pops in pops_grouped]))


        for pop in self.location.pops:
            # print("\nPop {} ({}):".format(pop.pop_job.title, pop.id))
            # print("Inventory: {}".format(pop.inventory.display()))

            # perform each Pop's production
            pop.money_yesterday = pop.money
            pop.perform_logic()

            # for each good, check to see if the Pop needs to buy or sell
            for good in Good.all():
                pop.generate_orders(good)

        for good in Good.all():
            self.resolve_orders(good)

        # resolve all offers for each Good
        for pop in self.location.pops:
            if pop.money < 0:
                # change to the most profitable pop type
                # unless there's an underserved market
                self.decide_new_pop_job(pop)




    def export(self):
        "Export the Market data as it currently exists"
        orders_for = lambda l, g: [o.export() for o in l[g]]
        return {
            'history': [{'good': good.ref(), 'data': self.history.export(good, 1)} for good in Good.all()],
            'most_demanded_good': self.most_demanded_good(),
            'most_profitable_pop_job': self.most_profitable_pop_job(),
            'most_expensive_good': self.most_costly_good(exclude=[Good.fish])
        }
