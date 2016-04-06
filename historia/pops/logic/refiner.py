from historia.pops.logic.logic_base import LogicBase
from historia.economy.enums.resource import Good

class RefinerLogic(LogicBase):

    def perform(self):
        bread = self.get_good(Good.bread)
        tools = self.get_good(Good.tools)
        iron_ore = self.get_good(Good.iron_ore)

        if bread is None or iron_ore is None:
            # fine $2 for being idle
            self.changeMoney(-2)
        elif tools is not None:
            # convert iron_ore to iron
            self.produce(Good.iron, 3)
            self.consume(Good.iron_ore, 1)
            self.consume(Good.bread, 1)
            self.consume(Good.tools, 1, 0.1)
        else:
            # convert iron_ore to iron
            self.produce(Good.iron, 1)
            self.consume(Good.iron_ore, 1)
            self.consume(Good.bread, 1)
