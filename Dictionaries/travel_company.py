transp_dict = {}

while True:
    city_transp_inp = input().split(':')
    if city_transp_inp[0] == 'ready':
        break
    transp_list = city_transp_inp[1].split(',')
    capacity_dict = {}
    for item in transp_list:
        items = item.split('-')
        capacity_dict[items[0]] = int(items[1])
    if city_transp_inp[0] in transp_dict.keys():
        for key, value in capacity_dict.items():
            transp_dict.get(city_transp_inp[0])[key] = value
    else:
        transp_dict[city_transp_inp[0]] = capacity_dict



while True:
    group_inp = input().split(' ')
    if group_inp[0] == 'travel':
        break
    for key, value in transp_dict.items():
        if key == group_inp[0]:
            if int(group_inp[1]) <= sum(value.values()):
                print(f'{key} -> all {group_inp[1]} accommodated')
            else:
                print(f'{key} -> all except {int(group_inp[1]) - sum(value.values())} accommodated')


# .get(group_inp[0])