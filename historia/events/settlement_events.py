def settle_hex(country):
    """
    For this country:
        Find a neighboring unowned hex
        If one exists, this event can fire
    """
    # find unowned neighboring hexes
    unowned_neighbors = set()
    for county in country.counties:
        unowned_neighbors.update(set(county.get_frontier_hexes()))

    # we have potential hexes
    if len(unowned_neighbors) > 0:
        # sort by settlement score
        # create a settlement
    else:
        # find overseas hexes
        return False
