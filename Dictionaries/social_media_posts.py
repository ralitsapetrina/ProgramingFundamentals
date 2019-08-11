all_posts_dict = {}

while True:
    command = input().split(' ')
    if command[0] == 'drop':
        break

    if command[0] == 'post':
        all_posts_dict[command[1]] = {'Likes': 0, 'Dislikes': 0, 'Comments': {}}
    elif command[0] == 'like':
        all_posts_dict[command[1]]['Likes'] += 1
    elif command[0] == 'dislike':
        all_posts_dict[command[1]]['Dislikes'] += 1
    elif command[0] == 'comment':
        all_posts_dict[command[1]]['Comments'].update({command[2]: ' '.join(command[3:])})

for key, value in all_posts_dict.items():
    print(f"Post: {key} | Likes: {value['Likes']} | Dislikes: {value['Dislikes']}")
    print("Comments:")
    if len(value['Comments']) == 0:
        print('None')
    else:
        for k_c, v_c in value['Comments'].items():
            print(f'*  {k_c}: {v_c}')