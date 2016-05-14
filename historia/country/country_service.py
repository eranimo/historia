import random
from historia.pops import make_initial_pops
from historia.country import Country, Province
from historia.world import give_hex_natural_resources

def find_good_unowned_hex(world_map):
    found = sorted(world_map.unowned_hexes, key=lambda h: h.favorability, reverse=True)
    if found:
        return found[0]
    print(world_map.unowned_hexes)
    raise Exception("Couldn't find a suitable hex")

def create_country(manager, world_map):
    start_hex = find_good_unowned_hex(world_map)

    # give the hex some natural resources
    give_hex_natural_resources(start_hex)

    country = Country(manager, start_hex)

    # Give that province pops and RGOs
    capital_province = country.provinces[0]
    pops = make_initial_pops(capital_province)
    capital_province.add_pops(pops)

    provinces = [capital_province]

    find_more = 5
    last_province = capital_province

    while find_more > 0:
        new_hex = last_province.get_frontier_hexes()
        if len(new_hex) > 0:
            give_hex_natural_resources(new_hex[0])
            new_province = country.settle_hex(new_hex[0])
            new_pops = make_initial_pops(new_province)
            pops.extend(new_pops)
            new_province.add_pops(new_pops)
            provinces.append(new_province)
            last_province = new_province
            find_more -= 1
        else:
            find_more = 0


    return country, provinces, pops
