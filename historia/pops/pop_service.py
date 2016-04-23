from historia.pops.models.pop import Pop
from historia.pops.enums.pop_type import PopType
from random import randint

def make_random_pop(province, pop_type, count=10, min_p=1000, max_p=5000):
    "Make a random pop at a particular province of a certain PopType"
    pops = []
    for i in range(count):
        pops.append(Pop(province, pop_type, randint(min_p, max_p)))
    return pops

def make_initial_pops(province):
    pops = []
    p1 = make_random_pop(province, PopType.farmer)
    p6 = make_random_pop(province, PopType.miner)
    p2 = make_random_pop(province, PopType.miller)
    p3 = make_random_pop(province, PopType.woodcutter)
    p4 = make_random_pop(province, PopType.blacksmith)
    p5 = make_random_pop(province, PopType.refiner)
    p7 = make_random_pop(province, PopType.baker)
    pops.extend(sum([p1, p2, p3, p4, p5, p6, p7], []))
    return pops
