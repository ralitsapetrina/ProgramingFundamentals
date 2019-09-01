data_list = list(map(int, input().split()))

def multiply_inlist(data_list, command_list):
    element = command_list[1]
    n = int(command_list[2])
    if element == 'list':
        data_list = data_list * n
    elif int(element) in data_list:
        while int(element) in data_list:
            data_list.remove(int(element))
            data_list.append(int(element) * n)
    return data_list

def contains_el(data_list, command_list):
    element = int(command_list[1])
    if element in data_list:
        print('True')
    else:
        print('False')

def add_el(data_list, command_list):
    element = list(map(int, command_list[1].split(',')))
    data_list.extend(element)
    return data_list



commands_dict = {'multiply': multiply_inlist, 'contains': contains_el, 'add': add_el}

while True:
    command_list = input().split()
    if command_list[0] == 'END':
        break
    if command_list[0] == 'multiply' or command_list[0] == 'add':
        data_list = commands_dict[command_list[0]](data_list, command_list)
    else:
        commands_dict[command_list[0]](data_list, command_list)

sorted_list = (sorted(data_list))

print(*sorted_list)