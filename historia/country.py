
class Country:
    """
        Representation of a Country
    """
    def __init__(self, ancestor=None, manager):
        self.manager = manager

        self._name_timeline = []
        self._name = TimelineProperty(self.manager, self._name_timeline)


        # ancestor country (mother country)
        # The country this country was formed out of
        self.ancestor = ancestor

    @property
    def name(self):
        return self._name.get(self.manager.current_day)

    @name.setter
    def name(self, value):
        self._name.set(self.manager.current_day, value)
