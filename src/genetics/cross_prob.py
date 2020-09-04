import random


def example_cross_prob_func(triangle):
    # return random.uniform(0, point.layer/10.0 + 0.06) > 0.05 and len(point.children) < 3
    return random.uniform(0, 10 / (triangle.layer + 1)) > 2

def example_cross_prob_func2(triangle):
    # return random.uniform(0, point.layer/10.0 + 0.06) > 0.05 and len(point.children) < 3
    return random.randint(0, triangle.layer**3+1) == 0
