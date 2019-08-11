import math

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


class Box:
    def __init__(self, up_left: Point, up_right: Point, bot_left: Point, bot_right: Point):
        self.up_left = up_left
        self.up_right = up_right
        self.bot_left = bot_left
        self.bot_right = bot_right


    def calc_width(self):
        width = Point.calc_distance(self.up_left, self.up_right)
        if width.is_integer():
            return int(width)
        else:
            return width

    def calc_height(self):
        height = Point.calc_distance(self.up_left, self.bot_left)
        if height.is_integer():
            return int(height)
        else:
            return height

    def calc_perimeter(self):
        return 2 * self.calc_width() + 2 * self.calc_height()

    def calc_area(self):
        return self.calc_width() * self.calc_height()

    def show_box(self):
        return f'Box: {self.calc_width()}, {self.calc_height()}\nPerimeter: {self.calc_perimeter()}\nArea: {self.calc_area()}'


def create_point(split_point_list):
    return Point(x=split_point_list[0], y=split_point_list[1])


def create_box(points_list):
    return Box(up_left=points_list[0],up_right=points_list[1], bot_left=points_list[2], bot_right=points_list[3])


boxes_list = []

while True:
    data_list = input().split(' | ')
    if data_list[0] == 'end':
        break

    point_list = []
    for item in data_list:
        new_point = create_point(list(map(float, item.split(':'))))
        point_list.append(new_point)

    new_box = create_box(point_list)
    boxes_list.append(new_box)


for box in boxes_list:
    print(box.show_box())