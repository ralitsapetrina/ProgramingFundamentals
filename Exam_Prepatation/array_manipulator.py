data_list = list(map(int, input().split()))

def exchange(data_list, command_list):
    index = int(command_list[1])
    if index >= len(data_list) or index < 0:
        print('Invalid index')
    list_1 = data_list[index + 1:]
    list_2 = data_list[:index + 1]
    final_list = list_1 + list_2
    return final_list

def filter_even_odd(type, data_list):
    if type == 'even':
        return list(filter(lambda x: x % 2 == 0, data_list))
    elif type == 'odd':
        return list(filter(lambda x: x % 2 == 1, data_list))

def max_min_num(data_list, command_list):
    max_min = command_list[0]
    type = command_list[1]
    element = 0
    filtered_list = filter_even_odd(type, data_list)
    if len(filtered_list) > 0:
        if max_min == 'max':
            element = max(filtered_list)
        elif max_min == 'min':
            element = min(filtered_list)
        print(len(data_list) - 1 - data_list[::-1].index(element))
    else:
        print('No matches')

def first_last_elements(data_list, command_list):
    first_last = command_list[0]
    count = int(command_list[1])
    type = command_list[2]
    if count > len(data_list):
        return print('Invalid count')
    filtered_list = filter_even_odd(type, data_list)
    if first_last == 'first':
        return print(filtered_list[:count])
    elif first_last == 'last':
        return print(filtered_list[-count:])


commands_dict = {'max': max_min_num, 'min': max_min_num, 'first': first_last_elements, 'last': first_last_elements}

while True:
    command_list = input().split()
    if command_list[0] == 'end':
        break
    if command_list[0] == 'exchange':
        data_list = exchange(data_list, command_list)
    else:
        commands_dict[command_list[0]](data_list, command_list)

print(data_list)