from points_model.point import Point
import numpy as np


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
        c1 = Point([], None, 0, 0)
        c1.set_xyrgb(0, 0, self.init_R, self.init_G, self.init_B)
        c2 = Point([], None, 0, 0)
        c2.set_xyrgb(1, 0, self.init_R, self.init_G, self.init_B)
        c3 = Point([], None, 0, 0)
        c3.set_xyrgb(1, 1, self.init_R, self.init_G, self.init_B)
        c4 = Point([], None, 0, 0)
        c4.set_xyrgb(0, 1, self.init_R, self.init_G, self.init_B)

        # definition of first descendants
        d1 = Point([c1, c2, c3], c2, 0, 0)
        d2 = Point([c1, c4, c3], c4, 0, 0)
        d1.recalculate_me()
        d1.set_rgb(self.init_R, self.init_G, self.init_B)
        d2.recalculate_me()
        d2.set_rgb(self.init_R, self.init_G, self.init_B)

        self.first_layer = [
            c1, c2, c3, c4
        ]

        self.second_layer = [
            d1, d2
        ]

        self.points_by_layer = [self.first_layer, self.second_layer]

        self.triangles = {d1: [0, 1, 2], d2: [0, 1, 2]}

    def find_points(self, probabilty_func):
        result = []
        for idx in range(1, len(self.points_by_layer)):
            for idx2 in range(len(self.points_by_layer[idx])):
                if probabilty_func(self.points_by_layer[idx][idx2]):
                    result.append(self.points_by_layer[idx][idx2])
        return result

    def add_three_points(self, point_leaf):
        point1 = Point([point_leaf, point_leaf.parents[1], point_leaf.parents[2]], point_leaf, 0, 0)
        point2 = Point([point_leaf.parents[0], point_leaf, point_leaf.parents[2]], point_leaf, 0, 0)
        point3 = Point([point_leaf.parents[0], point_leaf.parents[1], point_leaf], point_leaf, 0, 0)
        if len(self.points_by_layer) - 1 <= point_leaf.layer:
            self.points_by_layer.append([point1, point2, point3])
        else:
            #print(str(point_leaf.layer))
            #print(str(len(self.points_by_layer)))
            self.points_by_layer[point_leaf.layer + 1].append(point1)
            self.points_by_layer[point_leaf.layer + 1].append(point2)
            self.points_by_layer[point_leaf.layer + 1].append(point3)

        del self.triangles[point_leaf]
        self.triangles[point1] = [0, 1, 2]
        self.triangles[point2] = [0, 1, 2]
        self.triangles[point3] = [0, 1, 2]

    def mutate_one(self, point):
        point.radius_percentage = self.mutation_range_function(0, 1, 1, point.radius_percentage)*0.7
        point.alfa = self.mutation_range_function(-99999999, 99999999, np.pi*2,  point.alfa)
        point.R = int(self.mutation_range_function(0, self.color_range, self.color_range, point.R))
        point.G = int(self.mutation_range_function(0, self.color_range, self.color_range, point.G))
        point.B = int(self.mutation_range_function(0, self.color_range, self.color_range, point.B))
        point.recalculate_me_and_descendants()

    def mutate_model(self):
        points_to_mutate = self.find_points(self.mutation_probability_func)
        for point in points_to_mutate:
            self.mutate_one(point)

    def cross_model(self):
        points_to_cross = self.find_points(self.cross_probability_func)
        for point in points_to_cross:
            self.add_three_points(point)

    def get_triangles(self):
        result = []
        for point in self.triangles:
            my_map1 = {'points': [(point.x, point.y)], 'colors': [(point.R, point.R, point.G), (), ()]}
            my_map2 = {'points': [(point.x, point.y)], 'colors': [(point.R, point.R, point.G), (), ()]}
            my_map3 = {'points': [(point.x, point.y)], 'colors': [(point.R, point.R, point.G), (), ()]}
            parent_idx = 0
            my_map1['points'].append((point.parents[parent_idx].x, point.parents[parent_idx].y))
            my_map1['points'].append((point.parents[(parent_idx + 1)%3].x, point.parents[(parent_idx + 1)%3].y))
            my_map1['colors'][1] = (point.parents[parent_idx].R, point.parents[parent_idx].G, point.parents[parent_idx].B)
            my_map1['colors'][2] = (point.parents[(parent_idx + 1)%3].R, point.parents[(parent_idx + 1)%3].G, point.parents[(parent_idx + 1)%3].B)
            parent_idx = 1
            my_map2['points'].append((point.parents[parent_idx].x, point.parents[parent_idx].y))
            my_map2['points'].append((point.parents[(parent_idx + 1)%3].x, point.parents[(parent_idx + 1)%3].y))
            my_map2['colors'][1] = (point.parents[parent_idx].R, point.parents[parent_idx].G, point.parents[parent_idx].B)
            my_map2['colors'][2] = (point.parents[(parent_idx + 1)%3].R, point.parents[(parent_idx + 1)%3].G, point.parents[(parent_idx + 1)%3].B)
            parent_idx = 2
            my_map3['points'].append((point.parents[parent_idx].x, point.parents[parent_idx].y))
            my_map3['points'].append((point.parents[(parent_idx + 1)%3].x, point.parents[(parent_idx + 1)%3].y))
            my_map3['colors'][1] = (point.parents[parent_idx].R, point.parents[parent_idx].G, point.parents[parent_idx].B)
            my_map3['colors'][2] = (point.parents[(parent_idx + 1)%3].R, point.parents[(parent_idx + 1)%3].G, point.parents[(parent_idx + 1)%3].B)
            result.append(my_map1)
            result.append(my_map2)
            result.append(my_map3)
        return result



