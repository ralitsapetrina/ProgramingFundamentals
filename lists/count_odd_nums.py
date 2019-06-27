list = list(map(int, input().split(" ")))
odd_nums = 0

for num in list:
    if not num % 2 == 0:
        odd_nums += 1

print(odd_nums)