list = list(map(int, input().split(" ")))
positive_numbers = []


for number in list:
    if not number < 0:
        positive_numbers.append(number)

if len(positive_numbers) > 0:
    print(*reversed(positive_numbers))
else:
    print('empty')