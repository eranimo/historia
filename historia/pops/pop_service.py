from historia.pops.models.pop import Pop
from historia.pops.enums.pop_job import PopJob
from random import randint

def make_random_pop(province, pop_job, count=10, min_p=1000, max_p=5000):
    "Make a random pop at a particular province of a certain PopJob"
    pops = []
    for i in range(count):
        pops.append(Pop(province, pop_job, randint(min_p, max_p)))
    return pops

def make_initial_pops(province):
    pops = []
    p1 = make_random_pop(province, PopJob.farmer)
    p6 = make_random_pop(province, PopJob.miner)
    p2 = make_random_pop(province, PopJob.miller)
    p3 = make_random_pop(province, PopJob.woodcutter)
    p4 = make_random_pop(province, PopJob.blacksmith)
    p5 = make_random_pop(province, PopJob.refiner)
    p7 = make_random_pop(province, PopJob.baker)
    p7 = make_random_pop(province, PopJob.merchant, count=5, min_p=10, max_p=500)
    pops.extend(sum([p1, p2, p3, p4, p5, p6, p7], []))
    return pops
