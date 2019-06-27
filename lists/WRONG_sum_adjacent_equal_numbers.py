list_input = input().split(" ")

l = []


def int_value(value):
    try:
        is_int = int(value)
    except ValueError:
        return False
    else:
        return True


for value in list_input:
    if int_value(value):
        l.append(int(value))
    else:
        l.append(float(value))

while True:
    is_equal_counter = 0
    new_list = []

    if len(l) == 2 and l[0] == l[1]:
        is_equal = l[num - 1] + l[num]
        l.clear()
        l.append(is_equal)

    for num in range(1, len(l)):
        if l[num] == l[num-1]:
            is_equal = l[num - 1] + l[num]
            l[num] = None
            l[num - 1] = None
            l.insert(num-1, is_equal)
            is_equal_counter += 1
            break
    if is_equal_counter == 0:
        break


print(*l)