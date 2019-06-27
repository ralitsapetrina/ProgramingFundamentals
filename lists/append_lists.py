list_of_lists = list(input().split("|"))

list = []

for index in range(len(list_of_lists)):
    temp_list = list_of_lists[index].split(" ")
    list.insert(0, temp_list)

new_list = []

for el in list:
    temp_list = new_list.extend(el)

final_list = []

for number in new_list:
    if number:
        final_list.append(number)

print(*final_list)