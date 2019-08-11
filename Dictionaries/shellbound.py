from math import ceil

shell_dict = {}


while True:
    shells = input().split(" ")

    if shells[0] == "Aggregate":
        break

    key = shells[0]
    value = [(shells[1])]

    if shells[0] in shell_dict.keys():
        if not shells[1] in shell_dict.get(shells[0]):
            shell_dict.get(shells[0]).append(shells[1])
    else:
        shell_dict[key] = value



for key, value in shell_dict.items():
    int_value_iter = list(map(int, value))
    giant_shell = sum(int_value_iter) - (sum(int_value_iter) / len(int_value_iter))
    print(f'{key} -> ', end='')
    print(', '.join(value), f'({ceil(giant_shell)})')
