class Rectangle:
    def __init__(self, top, left, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.bottom = self.calc_bottom()
        self.right = self.calc_right()

    def calc_bottom(self):
        return self.top + self.width

    def calc_right(self):
        return self.left + self.height


def is_inside(r_1: Rectangle, r_2: Rectangle):
    if r_1.left >= r_2.left and r_1.right <= r_2.right and r_1.top >= r_2.top and r_1.bottom <= r_2.bottom:
        return 'Inside'
    else:
        return 'Not inside'


rect_1 = Rectangle(*list(map(int, input().split())))
rect_2 = Rectangle(*list(map(int, input().split())))

print(is_inside(rect_1, rect_2))