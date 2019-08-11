n = int(input())
counter = 0
clothes_dict = {}

while counter < n:
    colors = input().split(" -> ")

    key = colors[0]
    value = colors[1].split(",")

    if key in clothes_dict.keys():
        clothes_dict.get(key).extend(value)
    else:
        clothes_dict[key] = value

    counter += 1

searching = input().split(" ")


def printing_output(dict, search):
    printed_values_list = []
    for key, value in dict.items():
        print(f'{key} clothes:')
        for items in value:
            if items in printed_values_list:
                continue
            if search[0] == key:
                if search[1] == items:
                    print(f'* {items} - {value.count(items)} (found!)')
                else:
                    print(f'* {items} - {value.count(items)}')
            else:
                print(f'* {items} - {value.count(items)}')
            printed_values_list.append(items)



printing_output(clothes_dict, searching)