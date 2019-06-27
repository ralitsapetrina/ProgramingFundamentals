import math

l = list(map(int, input().split(" ")))

squares = []

for square in l:
    if square > 0:
        if math.sqrt(square) == int(math.sqrt(square)):
            squares.append(square)

squares.sort(reverse=True)


print(*squares)