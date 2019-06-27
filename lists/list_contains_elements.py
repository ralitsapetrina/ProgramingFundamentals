list = list(map(int, input().split(" ")))
n = int(input())
is_in_list = False

for checking in list:
    if checking == n:
        is_in_list = True

if is_in_list:
    print('yes')
else:
    print('no')