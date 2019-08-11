import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(point_1: Point, point_2: Point):
    side_a = abs(point_1.x - point_2.x)
    side_b = abs(point_1.y - point_2.y)

    return print(f'{(math.sqrt(side_a ** 2 + side_b ** 2)):.3f}')



x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())

point_1 = Point(x_1, y_1)
point_2 = Point(x_2, y_2)

calc_distance(point_1, point_2)