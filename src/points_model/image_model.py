from src.points_model.point import Point


class ImageModel:

    init_R = 1
    init_G = 1
    init_B = 1

    def __init__(self):

        # definition of points on the corners of image
        c1 = Point([], 0, 0)
        c1.set_xyrgb(0, 0, self.init_R, self.init_G, self.init_B)
        c2 = Point([], 0, 0)
        c2.set_xyrgb(1, 0, self.init_R, self.init_G, self.init_B)
        c3 = Point([], 0, 0)
        c3.set_xyrgb(1, 1, self.init_R, self.init_G, self.init_B)
        c4 = Point([], 0, 0)
        c4.set_xyrgb(0, 1, self.init_R, self.init_G, self.init_B)

        # definition of first descendants
        d1 = Point([c1, c2, c3], 0, 0)
        d2 = Point([c1, c4, c3], 0, 0)

        self.first_layer = [
            c1, c2, c3, c4
        ]

        self.second_layer = [
            d1, d2
        ]

        self.point_leaves = [d1, d2]   # deepest points in the city




