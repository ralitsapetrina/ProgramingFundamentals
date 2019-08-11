data_list = input().split(" : ")

phone_dict = {}

while not data_list[0] == "Over":
    if data_list[0].isdigit():
        value = data_list[0]
        key = data_list[1]
    elif data_list[1].isdigit():
        value = data_list[1]
        key = data_list[0]

    phone_dict[key] = value
    data_list = input().split(" : ")

for key, value in sorted(phone_dict.items()):
    print(f'{key} -> {value}')
