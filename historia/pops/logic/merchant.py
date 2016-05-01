from historia.pops.logic.logic_base import LogicBase
from historia.economy.enums.resource import Good, NaturalResource

DEBUG = False

class MerchantLogic(LogicBase):

    @property
    def can_work(self):
        return True

    def perform(self):
        if DEBUG: print("Merchant: {} at {} (home: {})".format(self.pop.id, self.pop.location.name, self.pop.home.name))
        bread = self.get_good(Good.bread)
        tools = self.get_good(Good.tools)

        if not self.pop.is_away or self.pop.trade_good is None or self.pop.money < 1:
            # find a new good to trade
            self.pop.decide_trade_plan()

        if DEBUG: print("\t{} @ {}".format(self.pop.trade_good, self.pop.trade_location))

        # if we have a trade location
        if self.pop.trade_location:
            if self.pop.location is not self.pop.trade_location:
                # not yet at trade location
                if DEBUG: print("\tTraveling to {}".format(self.pop.trade_location.name))
                self.pop.go_to_province(self.pop.trade_location)
            else:
                # we're at trade location, allow trading
                if DEBUG: print("\tReached target province {}".format(self.pop.trade_location.name))

                # if we waited a few days and we can't get trade_good,
                # look for a new trade_good
                if self.pop.trading_days > 3:
                    self.pop.decide_trade_plan()
                    self.pop.trading_days = 0
                else:
                    self.pop.trading_days += 1

        else:
            if DEBUG: print("\tIdle since we can't trade")
            self.charge_idle_money()

        self.consume(Good.bread, 1)

        if DEBUG: print("\n")
