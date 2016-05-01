from historia.pops.logic.logic_base import LogicBase
from historia.economy.enums.resource import Good

class FarmerLogic(LogicBase):

    @property
    def can_work(self):
        return self.pop.location.hex.biome.can_farm

    def compute_yield(self, has_tools):
        base = 2

        if has_tools:
            base *= 2

        if self.pop.location.hex.has_river:
            base += 3

        return base

    def perform(self):
        bread = self.get_good(Good.bread)
        timber = self.get_good(Good.timber)
        tools = self.get_good(Good.tools)

        if timber is None or bread is None or not self.can_work:
            # fine $2 for being idle
            self.charge_idle_money()
        elif tools is not None:
            # no tools
            self.produce(Good.grain, self.compute_yield(True))
            self.consume(Good.bread, 1)
            self.consume(Good.timber, 1)
            self.consume(Good.tools, 1, 0.2)
        else:
            # tools and timber
            self.produce(Good.grain, self.compute_yield(False))
            self.consume(Good.bread, 1)
            self.consume(Good.timber, 1)
