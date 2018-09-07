import random


def random(*, low=0, high=1):
    assert high >= low
    n = high - low
    r = random.random() * n
    return low + r


def choice(lst):
    return random.choice(lst)