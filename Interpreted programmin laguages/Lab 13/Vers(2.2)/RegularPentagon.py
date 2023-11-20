from math import *
from Shape import Shape


class RegularPentagon(Shape):
    s_list = []

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, name):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.x5 = y5
        self.y5 = y5
        self.name = name
        self.s_list = [(self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3), (self.x4, self.y4), (self.x5, self.y5)]

    def square(self, s_list):
        x2 = s_list[1][0]
        x1 = s_list[0][0]
        y1 = s_list[0][1]
        y2 = s_list[1][1]
        side_length = sqrt(abs(pow(x2 - x1, 2) + pow(y2 - y1, 2)))
        return (side_length ** 2 * sqrt(25 + 10 * sqrt(5))) / 4

    def perimeter(self, s_list):
        x2 = s_list[1][0]
        x1 = s_list[0][0]
        y1 = s_list[0][1]
        y2 = s_list[1][1]
        side_length = sqrt(abs(pow(x2 - x1, 2) + pow(y2 - y1, 2)))
        return 5 * side_length

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