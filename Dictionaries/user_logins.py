login_dict = {}

while True:
    user_pass = input().split(" -> ")

    if user_pass[0] == "login":
        break

    login_dict[user_pass[0]] = user_pass[1]

bad_log = 0

while True:
    user_pass = input().split(" -> ")

    if user_pass[0] == "end":
        break

    if user_pass[0] in login_dict.keys() and user_pass[1] == login_dict.get(user_pass[0]):
        print(f'{user_pass[0]}: logged in successfully')
    elif user_pass[0] not in login_dict.keys() or user_pass[1] != login_dict.get(user_pass[0]):
        print(f'{user_pass[0]}: login failed')
        bad_log += 1

print(f'unsuccessful login attempts: {bad_log}')