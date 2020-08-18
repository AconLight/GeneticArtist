


class Point:

    def __init__(self, parents, radius_percentage, alfa):
        self.children = []  # the children points - used to recalculate data
        self.parents = parents  # the three points within which the point exists
        self.radius_percentage = radius_percentage  # the percentage of the possible radius of displacement of the
                                                    # point from the calculated center of its parents
        self.alfa = alfa    # the angle of the radius of the displacement
        self.recalculate_me()

    def set_xyrgb(self, x, y, R, G, B):
        self.x = x  # position X of point (0 - 1)
        self.y = y  # position Y of point (0 - 1)
        self.R = R  # red color of RGB system
        self.G = G  # green color of RGB system
        self.B = B  # blue color of RGB system

    def recalculate_me(self):
        # TODO calc x, y, RGB
        pass

    def recalculate_me_and_descendants(self):
        self.recalculate_me()
        for child in self.children:
            child.recalculate_me_and_descendants()

    def attach_child(self, point):
        self.children.append(point)
