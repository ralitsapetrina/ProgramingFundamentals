def top_bottom(num):
    for dash in range(num):
        print('--', end='')
    print()


def middle(num):
    print("-", end='')
    for mid_part in range(1, num):
        print("\/", end='')
    print("-")


def filled_square(num):
    top_bottom(num)
    for mid_part in range(2, num):
        middle(num)
    top_bottom(num)


if __name__ == "__main__":
    number = int(input())
    filled_square(number)