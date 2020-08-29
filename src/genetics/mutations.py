import random


def example_mutation_func(my_min, my_max, my_range, prev_value):
    val = prev_value + random.uniform(-my_range, my_range)
    if val < my_min:
        val = my_max + (val - my_min)
    if val > my_max:
        val = my_min + (my_max - val)
    return val
