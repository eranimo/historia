from enum import Enum

# DIPLOMATIC

class Attitude(Enum):
    none = 'None'
    hostile = 'Hostile'
    outraged = 'Outraged'
    threatened = 'Threatened'
    neutral = 'Neutral'
    friendly = 'Friendly'


# GOVERNMENT

class GovernmentType(Enum):
    monarchy = 'Monarchy'
    republic = 'Republic'
    theocracy = 'Theocracy'

class PrimaryDivisionTypes(Enum):
    province = 'Province' # unitary
    department = 'Department' # unitary
    state = 'State' # federal
    territory = 'Territory' # dependant territory
    colonial = 'Colonial' # colonial unit

class SecondaryDivisionTypes(Enum):
    county = 'County'
    division = 'Division'
    department = 'Department'

class EthnicComposition(Enum):
    multiethnic = 'Multiethnic'
    nation_state = 'Nation State'

class DemocraticSystem(Enum):
    parliamentary = 'Parliamentary'
    presidential = 'Presidential'
    semipresidential = 'Semi-Presidential'

class CentralGovernmentTitle(Enum):
    central = 'Central'
    federal = 'Federal'
    imperial = 'Imperial'

class GovernmentStructure(Enum):
    # each province has sovereignty, but the central government has some powers
    confederal = 'Confederation'

    # central government has all the powers, provinces have no powers
    empire = 'Empire'

    # power is shared between the provinces (states) and central government
    federal = 'Federal'

    # the state has all the power
    unitary = 'Unitary'

class EmpireTypes(Enum):
    # land based empires with no colonies
    classical = 'Classical'
    # empire with colonies
    colonial = 'Colonial'


# POLITICS

class PartySystem(Enum):
    non_partisan = 'Non-partisan'
    one_party = 'One-party'
    dominant_party = 'Dominant-party'
    two_party = 'Two-party'
    multi_party = 'Multi-party'

class PartyPlatform(Enum):
    extremist_radical = 'Extremist Radical'
    reformist_moderate = 'Reformist Moderate'
    syncretic = 'Syncretic'
    conservative_reactionary = 'Conservative Reactionary'
    fundamentalist = 'Fundamentalist'

class PartySpectrum(Enum):
    far_left = 'Far-left'
    left = 'Left'
    center_left = 'Center-left'
    center = 'Center'
    center_right = 'Center-right'
    right = 'Right'
    far_right = 'Far-right'


# PROVINCE_TITLES = {
#     GovernmentStructure.federal: ProvinceTitles.state,
#     GovernmentStructure.empire: ProvinceTitles.province,
#     GovernmentStructure.unitary: ProvinceTitles.province
# }
