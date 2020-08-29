
from points_model.point import Point

class Triangle:

    def __init__(self, points, parent):
        self.points = points
        self.parent = parent

    def create_children(self):
        point1 = Point([self.points[0], self.points[1]], 0.5)
        point2 = Point([self.points[1], self.points[2]], 0.5)
        point3 = Point([self.points[2], self.points[0]], 0.5)
        triangle0 = Triangle([point1, point2, point3], self)
        triangle1 = Triangle([point1, point2, self.points[1]], self)
        triangle2 = Triangle([point2, point3, self.points[2]], self)
        triangle3 = Triangle([point3, point1, self.points[0]], self)

        return [triangle0, triangle1, triangle2, triangle3]
