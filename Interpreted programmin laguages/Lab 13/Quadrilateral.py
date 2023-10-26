from math import *
from Shape import Shape


class Quadrilateral(Shape):
    s_list = []

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, name):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.name = name
        self.s_list = [(self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3), (self.x4, self.y4)]

    def square(self, s_list):
        x1 = s_list[0][0]
        x2 = s_list[1][0]
        x3 = s_list[2][0]
        y1 = s_list[0][1]
        y2 = s_list[1][1]
        y3 = s_list[2][1]
        x4 = s_list[3][0]
        y4 = s_list[3][1]
        a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        c = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        d = sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
        p = (a + b + c + d) / 2
        return sqrt((p - a) * (p - b) * (p - c) * (p - d))

    def perimeter(self, s_list):
        x1 = s_list[0][0]
        x2 = s_list[1][0]
        x3 = s_list[2][0]
        y1 = s_list[0][1]
        y2 = s_list[1][1]
        y3 = s_list[2][1]
        x4 = s_list[3][0]
        y4 = s_list[3][1]
        a = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        c = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        d = sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
        return a + b + c + d

    def move(self, x, y):
        self.x1 += x
        self.y1 += y
        self.x2 += x
        self.y2 += y
        self.x3 += x
        self.y3 += y
        self.x4 += x
        self.y4 += y
        print("Фигура смещена на (" + x + ";" + y + ")")

    def fill(self, color):
        self.color = color
