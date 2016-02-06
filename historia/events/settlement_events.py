def settle_hex(country):
    """
    For this country:
        Find a neighboring unowned hex
        If one exists, this event can fire
    """
    unowned_neighbors = set()
    for h in country.territory:
        unowned_neighbors.update(set([n for n in h.neighbors if n.owner is None]))
