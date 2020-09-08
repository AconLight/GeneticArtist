import random
import math


def select_probable_points(points):
    probable_points = []
    for point in points:
        if random.randint(0, int(math.sqrt(len(point.children)))) == 0:
            probable_points.append(point)
    return probable_points


def all_mutate(points):
    return select_probable_points(points)


def some_mutate(points):
    probable_points = select_probable_points(points)
    if len(probable_points) == 0:
        return []
    return random.sample(probable_points, int(math.sqrt(random.randint(0, len(probable_points)))))


def one_mutate(points):
    probable_points = select_probable_points(points)
    if len(probable_points) == 0:
        return []
    return [random.choice(probable_points)]
