import math
import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def print_point(self):
        return f'({self.x}, {self.y})'


def calc_distance(point_1, point_2):
    side_a = abs(point_1.x - point_2.x)
    side_b = abs(point_1.y - point_2.y)

    return math.sqrt(side_a ** 2 + side_b ** 2)

def format_min_result(res, p_1, p_2):
    return f'{res:.3f}\n{p_1.print_point()}\n{p_2.print_point()}'

n = int(input())
counter = 0
point_list = []
min_result = sys.maxsize
close_point_1 = None
close_point_2 = None

while counter < n:
    counter += 1
    x, y = list(map(int, input().split()))
    point = Point(x, y)
    point_list.append(point)

for p_1 in range(len(point_list)):
    for p_2 in range(p_1 + 1, len(point_list)):
        result = calc_distance(point_list[p_1], point_list[p_2])
        if result < min_result:
            min_result = result
            close_point_1 = point_list[p_1]
            close_point_2 = point_list[p_2]


print(format_min_result(min_result, close_point_1, close_point_2))
