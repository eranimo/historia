from historia.economy import RGO, RGOType

def make_RGOs(province, rgo_type, owner, employee):
    "Make a RGO at the province"
    return RGO(province, rgo_type, owner, employee)
