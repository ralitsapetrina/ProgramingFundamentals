data_dict = {}


while True:
    data_list = input().split((' -> '))
    if data_list[0] == 'end':
        break

    values_list = data_list[1].split(', ')

    if not values_list[0].isdigit():
        if data_list[1] in data_dict.keys():
            value = data_dict.get(data_list[1]).copy()
            data_dict[data_list[0]] = value
    else:
        if not data_list[0] in data_dict.keys():
            data_dict[data_list[0]] = values_list
        else:
            data_dict.get(data_list[0]).extend(values_list)

for key, value in data_dict.items():
    print(f'{key} ===', ', '.join(value))