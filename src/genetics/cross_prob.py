import random


def example_cross_prob_func(triangle):
    # return random.uniform(0, point.layer/10.0 + 0.06) > 0.05 and len(point.children) < 3
    return random.randint(0, 1 + triangle.layer) < 5 and random.randint(0, 2) == 0
