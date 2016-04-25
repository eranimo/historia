from historia.pops.logic.logic_base import LogicBase
from historia.economy.enums.resource import Good, NaturalResource
from historia.world import Biome


class WoodcutterLogic(LogicBase):

    @property
    def can_work(self):
        has_timber = self.pop.province.hex.has_natural_resource(NaturalResource.trees)
        return has_timber

    def perform(self):
        bread = self.get_good(Good.bread)
        tools = self.get_good(Good.tools)

        if bread is None or not self.can_work:
            # fine $2 for being idle
            self.charge_idle_money()
        elif tools is None:
            # no tools
            self.produce(Good.timber, 4)
            self.consume(Good.bread, 1)
            self.consume(Good.tools, 1, 0.1)
        else:
            # tools and bread
            self.produce(Good.timber, 2)
            self.consume(Good.bread, 1)
