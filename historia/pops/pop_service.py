from historia.pops.models.pop import Pop
from historia.pops.enums.pop_type import PopType
from random import randint

def make_random_pop(province, pop_type, min_p=1e4, max_p=2e4):
    "Make a random pop at a particular province of a certain PopType"
    return Pop(province, pop_type, randint(min_p, max_p))
