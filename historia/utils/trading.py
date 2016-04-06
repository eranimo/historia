def position_in_range(value, r_min, r_max, clamp=True):
    "Get the value between a range of numbers given a mean value"
    value -= r_min
    r_max -= r_min
    r_min = 0
    value = value / (r_max - r_min)
    if clamp: # make value between 0 and 1
        if value < 0:
            value = 0
        if value > 1:
            value = 1
    return value
