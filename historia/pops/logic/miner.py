from historia.pops.logic.logic_base import LogicBase
from historia.economy.enums.resource import Good, NaturalResource

class MinerLogic(LogicBase):

    @property
    def can_work(self):
        return self.pop.location.hex.has_natural_resource(NaturalResource.iron)

    def perform(self):
        bread = self.get_good(Good.bread)
        tools = self.get_good(Good.tools)

        if bread is None or not self.can_work:
            # fine $2 for being idle
            self.charge_idle_money()
        elif tools is not None:
            # no tools
            self.produce(Good.iron_ore, 4)
            self.consume(Good.bread, 1)
            self.consume(Good.tools, 1, 0.1)
        else:
            # tools and bread
            self.produce(Good.iron_ore, 2)
            self.consume(Good.bread, 1)
