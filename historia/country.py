
class Country:
    """
        Representation of a Country
    """
    def __init__(self, manager):
        self.manager = manager

        self._name_timeline = []
        self._name = TimelineProperty(self.manager, self._name_timeline)

    @property
    def name(self):
        return self._name.get(self.manager.current_day)

    @name.setter
    def name(self, value):
        self._name.set(self.manager.current_day, value)
