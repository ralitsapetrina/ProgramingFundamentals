list = list(map(int, input(). split(" ")))

for index in range(1, len(list), 2):
    if not list[index] % 2 == 0:
        print(f'Index {index} -> {list[index]}')