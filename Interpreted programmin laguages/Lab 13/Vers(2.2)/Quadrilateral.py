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
        self.s_list = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

    def square(self, s_list):
        x_1, y_1 = s_list[0]
        x_2, y_2 = s_list[1]
        x_3, y_3 = s_list[2]
        x_4, y_4 = s_list[3]
        a = sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
        b = sqrt((x_3 - x_2) ** 2 + (y_3 - y_2) ** 2)
        c = sqrt((x_4 - x_3) ** 2 + (y_4 - y_3) ** 2)
        d = sqrt((x_1 - x_4) ** 2 + (y_1 - y_4) ** 2)
        p = (a + b + c + d) / 2
        return sqrt((p - a) * (p - b) * (p - c) * (p - d))

    def perimeter(self, s_list):
        x_1, y_1 = s_list[0]
        x_2, y_2 = s_list[1]
        x_3, y_3 = s_list[2]
        x_4, y_4 = s_list[3]
        a = sqrt(pow(abs(x_2 - x_1), 2) + pow(abs(y_2 - y_1), 2))
        b = sqrt(pow(abs(x_3 - x_2), 2) + pow(abs(y_3 - y_2), 2))
        c = sqrt((x_4 - x_3) ** 2 + (y_4 - y_3) ** 2)
        d = sqrt((x_1 - x_4) ** 2 + (y_1 - y_4) ** 2)
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
