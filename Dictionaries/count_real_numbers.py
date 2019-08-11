number_list = list(map(float, input().split()))

occ_dict = {num: number_list.count(num) for num in number_list}

for key, value in sorted(occ_dict.items()):
    print(f'{key} -> {value} times')