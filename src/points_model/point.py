import numpy as np


class Point:

    def __init__(self, parents, father, radius_percentage, alfa):
        self.children = []  # the children points - used to recalculate data
        for parent in parents:
            parent.children.append(self)

        if father is not None:
            self.layer = father.layer + 1
        else:
            self.layer = 0

        self.father = father
        self.parents = parents  # the three points within which the point exists
        self.radius_percentage = radius_percentage  # the percentage of the possible radius of displacement of the
                                                    # point from the calculated center of its parents
        self.alfa = alfa    # the angle of the radius of the displacement
        self.x = 0
        self.y = 0
        self.R = 0
        self.G = 0
        self.B = 0
        self.recalculate_me()

    def set_rgb(self, R, G, B):
        self.R = R  # red color of RGB system
        self.G = G  # green color of RGB system
        self.B = B  # blue color of RGB system

    def set_xyrgb(self, x, y, R, G, B):
        self.x = x  # position X of point (0 - 1)
        self.y = y  # position Y of point (0 - 1)
        self.R = R  # red color of RGB system
        self.G = G  # green color of RGB system
        self.B = B  # blue color of RGB system

    def recalculate_me(self):
        # TODO calc x, y
        if len(self.parents) == 0:
            return
        # calculating distances to parents
        d1 = np.sqrt((self.parents[0].x - self.x)*(self.parents[0].x - self.x) + (self.parents[0].y - self.y)*(self.parents[0].y - self.y))
        d2 = np.sqrt((self.parents[1].x - self.x)*(self.parents[1].x - self.x) + (self.parents[1].y - self.y)*(self.parents[1].y - self.y))
        d3 = np.sqrt((self.parents[2].x - self.x)*(self.parents[2].x - self.x) + (self.parents[2].y - self.y)*(self.parents[2].y - self.y))

        # calculating max radius
        radiuses = [d1, d2, d3]
        max_radius = np.min(radiuses)/2

        # calculating new x, y
        self.x = (self.parents[0].x + self.parents[1].x + self.parents[2].x) / 3 + self.radius_percentage*max_radius*np.cos(self.alfa)
        self.y = (self.parents[0].y + self.parents[1].y + self.parents[2].y) / 3 + self.radius_percentage*max_radius*np.sin(self.alfa)

    def recalculate_me_and_descendants(self):
        self.recalculate_me()
        for child in self.children:
            child.recalculate_me_and_descendants()

    def attach_child(self, point):
        self.children.append(point)
