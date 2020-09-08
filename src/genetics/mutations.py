import random


def example_mutation_func(my_min, my_max, my_range, prev_value):
    val = prev_value + random.uniform(-my_range, my_range)
    return (val-my_min) % (my_max - my_min) + my_min


def mirror_mutation_func(my_min, my_max, my_range, prev_value):
    val = prev_value + random.uniform(-my_range, my_range)
    return my_max - ((val - my_min) % (my_max - my_min) + my_min) + my_min
