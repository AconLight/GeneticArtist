import numpy as np
import random

class Point:

    def __init__(self, fathers, radius_percentage):
        self.children = []  # the children points - used to recalculate data
        self.mutations_numb = 0
        if len(fathers) != 0:
            self.layer = fathers[0].layer + 1
            self.R = (fathers[0].R + fathers[1].R) / 2
            self.G = (fathers[0].G + fathers[1].G) / 2
            self.B = (fathers[0].B + fathers[1].B) / 2
            for f in fathers:
                f.children.append(self)
        else:
            self.layer = 0
            self.R = 255 #random.randint(0, 255)
            self.G = self.R
            self.B = self.R
            # self.G = random.randint(0, 255)
            # self.B = random.randint(0, 255)

        self.fathers = fathers
        self.radius_percentage = radius_percentage  # the percentage of the possible radius of displacement of the
                                                    # point from the calculated center of its parents
        self.x = 0
        self.y = 0
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
        if len(self.fathers) == 0:
            return
        # calculating new position
        self.x = self.fathers[0].x * self.radius_percentage + self.fathers[1].x * (1 - self.radius_percentage)
        self.y = self.fathers[0].y * self.radius_percentage + self.fathers[1].y * (1 - self.radius_percentage)

    def recalculate_me_and_descendants(self):
        self.recalculate_me()
        for child in self.children:
            child.recalculate_me_and_descendants()

    def attach_child(self, point):
        self.children.append(point)
