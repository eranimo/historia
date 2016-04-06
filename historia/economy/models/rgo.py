class RGO(object):
    def __init__(self, province, rgo_type, owner, employee):
        """
        province (SecondaryDivision)
        rgo_type (RGOType)
        """
        self.province = province

        self.rgo_type = rgo_type

        self.owner = owner # the Pop that owns this RGO
        self.employee = employee # the Pop that works here

    def perform_production(self):
        """
        produce the raw goods
        give them to the owners inventory
        """
        pass
