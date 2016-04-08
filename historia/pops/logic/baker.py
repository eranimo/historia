from historia.pops.logic.logic_base import LogicBase
from historia.economy.enums.resource import Good

class BakerLogic(LogicBase):

    def perform(self):
        grain = self.get_good(Good.grain)

        if grain is None:
            # fine $2 for being idle
            self.charge_idle_money()
        else:
            # convert all grain to bread
            self.produce(Good.bread, grain.amount * 2)
            self.consume(Good.grain, grain.amount)
