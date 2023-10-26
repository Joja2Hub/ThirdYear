import math

from RegularPentagon import RegularPentagon
from Rhombus import Rhombus
from Quadrilateral import Quadrilateral

finish_list = []
shape_list = [
    # Четырехугольники
    [
        [(0, 0), (1, 0), (1, 1), (0, 1), "Quadrilateral1"],
        [(2, 2), (3, 2), (3, 3), (2, 3), "Quadrilateral2"],
        [(0, 0), (2, 1), (0, 2), (-2, 1), "Quadrilateral3"],
        [(1, 1), (3, 1), (3, 3), (1, 3), "Quadrilateral4"],
        [(-1, -1), (1, -1), (1, 1), (-1, 1), "Quadrilateral5"],

    ],
    # Ромбы
    [
        [(1, 1), (2, 0), (3, 1), (2, 2), "Rhombus1"],
        [(4, 0), (5, 1), (4, 2), (3, 1), "Rhombus2"],
        [(0, 0), (2, 1), (0, 2), (-2, 1), "Rhombus3"],
        [(-1, -1), (1, 0), (-1, 1), (-3, 0), "Rhombus4"],
        [(2, 3), (4, 4), (2, 5), (0, 4), "Rhombus5"],
    ],
    # Правильные пятиугольники
    [
        [(2, 4), (3, 5), (5, 5), (6, 4), (4, 3), "RegularPentagon1"],
        [(1, 2), (0, 4), (2, 5), (4, 3), (3, 1), "RegularPentagon2"],
        [(0, 0), (1, -2), (3, -2), (4, 0), (2, 2), "RegularPentagon3"],
        [(2, 2), (3, 0), (5, 0), (6, 2), (4, 4), "RegularPentagon4"],
        [(2, 3), (3, 1), (5, 1), (6, 3), (4, 5), "RegularPentagon5"]

    ],
]

colors = ["red", "blue", "grey", "orange", "black", "yellow"]

for i in range(len(shape_list)):
    if i < 5:
        x1 = shape_list[i][0][0]
        y1 = shape_list[i][0][1]
        x2 = shape_list[i][1][0]
        y2 = shape_list[i][1][1]
        x3 = shape_list[i][2][0]
        y3 = shape_list[i][2][1]
        x4 = shape_list[i][3][0]
        y4 = shape_list[i][3][1]
        name = shape_list[i][4]
        quad = Quadrilateral(x1, y1, x2, y2, x3, y3, x4, y4, name)
        finish_list.append(quad)
    elif 4 < i < 10:
        x1 = shape_list[i][0][0]
        y1 = shape_list[i][0][1]
        x2 = shape_list[i][1][0]
        y2 = shape_list[i][1][1]
        x3 = shape_list[i][2][0]
        y3 = shape_list[i][2][1]
        x4 = shape_list[i][3][0]
        y4 = shape_list[i][3][1]
        name = shape_list[i][4]
        rhomb = Quadrilateral(x1, y1, x2, y2, x3, y3, x4, y4, name)
        finish_list.append(rhomb)
    elif 10 < i:
        x1 = shape_list[i][0][0]
        y1 = shape_list[i][0][1]
        x2 = shape_list[i][1][0]
        y2 = shape_list[i][1][1]
        x3 = shape_list[i][2][0]
        y3 = shape_list[i][2][1]
        x4 = shape_list[i][3][0]
        y4 = shape_list[i][3][1]
        x5 = shape_list[i][4][0]
        y5 = shape_list[i][4][1]
        name = shape_list[i][5]
        penta = RegularPentagon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, name)
        finish_list.append(penta)

for i in range(len(finish_list)):
    print("Периметры фигур: ")
    print(str(finish_list[i].perimeter(finish_list[i].s_list) + " - " + finish_list[i].name))