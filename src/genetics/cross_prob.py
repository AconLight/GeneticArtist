import random


def example_cross_prob_func(point):
    return random.randint(0, 1) == 0 and len(point.children) < 3
