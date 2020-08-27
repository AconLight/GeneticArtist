import random


def example_mutation_func(my_min, my_max, my_range, prev_value):
    return (prev_value + random.uniform(my_min, my_max)*0.4*(random.randint(0, 1)*2-1)) % my_range
