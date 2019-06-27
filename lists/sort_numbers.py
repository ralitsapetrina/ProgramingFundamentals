l = list(map(float, (input().split(" "))))

l.sort()

for sorting in range(len(l)):
    if sorting == len(l) - 1:
        print(l[sorting])
    else:
        print(f'{l[sorting]} <= ', end="")
