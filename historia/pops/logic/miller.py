from historia.pops.logic.logic_base import LogicBase
from historia.economy.enums.resource import Good

class MillerLogic(LogicBase):

    def perform(self):
        bread = self.get_good(Good.bread)
        timber = self.get_good(Good.timber)
        tools = self.get_good(Good.tools)

        if timber is None or bread is None:
            # fine $2 for being idle
            self.charge_idle_money()
        elif tools is not None:
            # convert all grain to bread
            self.produce(Good.lumber, timber.amount)
            self.consume(Good.timber, timber.amount)
            self.consume(Good.bread, 1)

        else: # no tools
            # convert all grain to bread
            self.produce(Good.lumber, int(timber.amount / 1))
            self.consume(Good.timber, int(timber.amount / 1))
            self.consume(Good.bread, 1)
