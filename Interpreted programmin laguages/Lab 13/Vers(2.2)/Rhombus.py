from math import *
from Shape import Shape


class Rhombus(Shape):
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
        x_1, y_1 = s_list[0]
        x_2, y_2 = s_list[1]
        x_3, y_3 = s_list[2]
        x_4, y_4 = s_list[3]
        diagonal1 = sqrt(pow(abs(y_2 - y_1), 2))
        diagonal2 = sqrt(pow(abs(x_3 - x_2), 2))
        return (diagonal1 * diagonal2) / 2

    def perimeter(self, s_list):
        x_1, y_1 = s_list[0]
        x_2, y_2 = s_list[1]
        x_3, y_3 = s_list[2]
        x_4, y_4 = s_list[3]
        side_length = sqrt(abs(pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2)))
        return 4 * side_length

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