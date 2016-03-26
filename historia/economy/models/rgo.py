class RGO(object):
    def __init__(self, province, rgo_type, owner, employee):
        """
        province (SecondaryDivision)
        rgo_type (RGOType)
        """
        self.province = province

        self.rgo_type = rgo_type

        self.max_employees = 40000

        self.owner = None # the Pop that owns this RGO
        self.employees = None # the Pops that are employed at this RGO

    def perform_production(self):
        """
        produce the raw goods
        give them to the owners inventory
        """
        pass
