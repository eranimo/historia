from historia.pops.logic.logic_base import LogicBase
from historia.economy.enums.resource import Good

class BlacksmithLogic(LogicBase):

    def perform(self):
        bread = self.get_good(Good.bread)
        lumber = self.get_good(Good.lumber)
        iron = self.get_good(Good.iron)

        if bread is None or iron is None or lumber is None:
            # fine $2 for being idle
            self.charge_idle_money()
        else:
            # 1 iron + 1 lumber = 1 tool
            self.produce(Good.tools, 1)
            self.consume(Good.iron, 1)
            self.consume(Good.lumber, 1)

            # consume bread
            self.consume(Good.bread, 1)
