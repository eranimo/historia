from statistics import mean


class TradeHistoryLog:
    "A list of a particular type of historically-relevant economic data"

    def __init__(self, name):
        self.name = name

        # a dictionary of Good: list
        self.record = {}

    def register(self, key):
        "Registers a new key in the record and creates a new list for it"
        if key not in self.record:
            self.record[key] = []

    def add(self, key, amount):
        "Adds a record to this HistoryLog"
        self.record[key].append(amount)

    def extend(self, key, amount):
        "Extend a record to this HistoryLog"
        self.record[key].extend(amount)

    def average(self, key, day_range=15):
        "Gets the average amount of the given Good's record in the last `range` days"
        if key in self.record:
            return mean(self.record[key][-day_range:])
        return 0


class TradeHistory:
    prices = TradeHistoryLog('prices')
    buy_orders = TradeHistoryLog('buy_orders')
    sell_orders = TradeHistoryLog('sell_orders')
    trades = TradeHistoryLog('trades')
    profit = TradeHistoryLog('profit')

    def register(self, good):
        self.prices.register(good)
        self.buy_orders.register(good)
        self.sell_orders.register(good)
        self.trades.register(good)
        self.profit.register(good)

    def export(self, good, days=30):
        return {
            'prices': self.prices.record[good][-days:],
            'buy_orders': self.buy_orders.record[good][-days:],
            'sell_orders': self.sell_orders.record[good][-days:],
            'trades': self.trades.record[good][-days:],
            'profit': self.profit.record[good][-days:]
        }
