data_list = input().split(" = ")

names_dict = {}

while not data_list[0] == "end":
    if data_list[1].isdigit():
        key = data_list[0]
        value = int(data_list[1])
        names_dict[key] = value
    else:
        if data_list[1] in names_dict.keys():
            key = data_list[0]
            value = int(names_dict[data_list[1]])
            names_dict[key] = value

    data_list = input().split(" = ")


for key, value in names_dict.items():
    print(f'{key} === {value}')