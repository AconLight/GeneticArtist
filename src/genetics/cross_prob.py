import random


def example_cross_prob_func(point):
    # return random.uniform(0, point.layer/10.0 + 0.06) > 0.05 and len(point.children) < 3
    return random.randint(0, 30) >= len(point.children) and len(point.children) < 3
