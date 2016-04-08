from historia.pops.logic.logic_base import LogicBase
from historia.economy.enums.resource import Good

class FarmerLogic(LogicBase):

    def perform(self):
        bread = self.get_good(Good.bread)
        timber = self.get_good(Good.timber)
        tools = self.get_good(Good.tools)

        if timber is None or bread is None:
            # fine $2 for being idle
            self.charge_idle_money()
        elif tools is not None:
            # no tools
            self.produce(Good.grain, 4)
            self.consume(Good.bread, 1)
            self.consume(Good.timber, 1)
            self.consume(Good.tools, 1, 0.1)
        else:
            # tools and timber
            self.produce(Good.grain, 2)
            self.consume(Good.bread, 1)
            self.consume(Good.timber, 1)
