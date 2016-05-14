from historia.pops.logic.logic_base import LogicBase
from historia.economy.enums.resource import Good, NaturalResource

DEBUG = True

class MerchantLogic(LogicBase):

    def perform(self):
        # If we're back home, find a new good to trade
        if not self.pop.is_away:
            self.pop.decide_trade_plan()

        if DEBUG: print("""Merchant {}
        \tLocation: {}
        \tHome: {}
        \tTrade Target: {}
        \tTrade Good: {}
        \tAmount: {}""".format(self.pop.id,
                                          self.pop.location.name,
                                          self.pop.home.name,
                                          self.pop.trade_location,
                                          self.pop.trade_good,
                                          self.pop.trade_amount))

        amount_trade_good = self.get_good(self.pop.trade_good)

        # if we have a trade location
        if self.pop.trade_location:
            if self.pop.location is not self.pop.trade_location:
                # not yet at trade location
                if DEBUG: print("\tTraveling to {}".format(self.pop.trade_location.name))
                self.pop.go_to_province(self.pop.trade_location)
            else:
                # we're at trade location, allow trading
                if DEBUG: print("\tReached target province {}".format(self.pop.trade_location.name))

                if amount_trade_good is not None:
                    # we have goods, go home at sell them
                    self.pop.go_to_province(self.pop.home)
                    # set the ideal to 0 so that we trade our goods
                    self.pop.inventory.set_ideal(self.pop.trade_good, 0)
                    if DEBUG: print("\tWe have goods, now we're going home")
                else:
                    if DEBUG: print("\tNow we're trading!")

        else:
            if DEBUG: print("\tIdle since we can't trade")
            self.pop.decide_trade_plan()
            self.charge_idle_money(charge=0.1)

        if self.pop.trade_success < 15:
            if DEBUG: print("\tPenalizing Merchant because he sucks")
            self.charge_idle_money(charge=1)

        # if we don't have bread, charge us
        if self.get_good(Good.bread) is not None:
            self.consume(Good.bread, 1)

        if DEBUG: print("\n")
