list = list(map(int, input().split(" ")))

list.sort()
new_list = []
occur = 0

for item in list:
    if item not in new_list:
        new_list.append(item)

for printing in new_list:
    print(f'{printing} -> {list.count(printing)}')