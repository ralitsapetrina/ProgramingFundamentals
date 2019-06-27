list = list(map(int, input().split(" ")))
n = int(input())
new_list = []

for num in list:
    new_list.append(num * n)

print(*new_list)