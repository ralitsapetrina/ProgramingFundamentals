key = input()
value = input()
n = int(input())

final_dict = {}

for item in range(n):
    search_input = input().split(' => ')
    value_list_search = search_input[1].split(';')
    value_list = [n for n in value_list_search if value in n]
    if key in search_input[0]:
        final_dict[search_input[0]] = value_list

for key, value in final_dict.items():
    print(f'{key}:')
    for v in value:
        print(f'-{v}')