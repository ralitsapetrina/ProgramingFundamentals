topics_dict = {}

while True:
    data_list = input().split(' -> ')
    if data_list[0] == 'filter':
        break
    tags_list = data_list[1].split(', ')
    if data_list[0] in topics_dict.keys():
        if not set(tags_list).issubset(topics_dict.get(data_list[0])):
            topics_dict.get(data_list[0]).extend(tags_list)
    else:
        topics_dict[data_list[0]] = tags_list

search_tags = input().split(', ')

for key, value in topics_dict.items():
    if set(search_tags).issubset(value):
        print_values = ['#' + n for n in value]
        print(f'{key} |', ', '.join(print_values))
