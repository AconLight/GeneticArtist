from points_model.point import Point
from points_model.triangle import Triangle
import numpy as np
import random

class ImageModel:

    color_range = 255

    init_R = color_range
    init_G = color_range
    init_B = color_range

    def __init__(self, mutation_probability_func, cross_probability_func, mutation_range_function):

        self.mutation_probability_func = mutation_probability_func
        self.cross_probability_func = cross_probability_func
        self.mutation_range_function = mutation_range_function

        # definition of points on the corners of image
        c1 = Point([], 0)
        c1.set_xyrgb(0, 0, self.init_R, self.init_G, self.init_B)
        c2 = Point([], 0)
        c2.set_xyrgb(1, 0, self.init_R, self.init_G, self.init_B)
        c3 = Point([], 0)
        c3.set_xyrgb(1, 1, self.init_R, self.init_G, self.init_B)
        c4 = Point([], 0)
        c4.set_xyrgb(0, 1, self.init_R, self.init_G, self.init_B)

        self.points = [
            c1, c2, c3, c4
        ]

        t1 = Triangle([c1, c2, c3], None)
        t2 = Triangle([c1, c4, c3], None)

        self.triangles = [t1, t2]

    def find_points(self, probabilty_func):
        result = []
        for point in self.points:
            if probabilty_func(point):
                result.append(point)
        return result

    def find_triangles(self, probabilty_func):
        result = []
        for triangle in self.triangles:
            if probabilty_func(triangle):
                result.append(triangle)
        return result

    def add_triangle(self, triangle):
        new_triangles = triangle.create_children()
        self.triangles.remove(triangle)
        for t in new_triangles:
            self.triangles.append(t)

        for p in new_triangles[0].points:
            self.points.append(p)

    def mutate_one(self, point):
        if random.randint(0, 1) == 0:
            point.radius_percentage = self.mutation_range_function(0.4, 0.6, 0.1, point.radius_percentage)
        else:
            point.R = int(self.mutation_range_function(0, self.color_range, self.color_range/4.0, point.R))
            point.G = point.R
            point.B = point.R
            # point.G = int(self.mutation_range_function(0, self.color_range, self.color_range, point.G))
            # point.B = int(self.mutation_range_function(0, self.color_range, self.color_range, point.B))

        point.recalculate_me_and_descendants()

    def mutate_model(self):
        points_to_mutate = self.find_points(self.mutation_probability_func)
        for point in points_to_mutate:
            self.mutate_one(point)

    def cross_model(self):
        triangles_to_cross = self.find_triangles(self.cross_probability_func)
        for triangle in triangles_to_cross:
            self.add_triangle(triangle)

    def get_triangles(self):
        result = []
        for t in self.triangles:
            result.append({'points': list(map(lambda point: (point.x, point.y), t.points)), 'colors': list(map(lambda point: (point.R, point.G, point.B), t.points))})

        return result
