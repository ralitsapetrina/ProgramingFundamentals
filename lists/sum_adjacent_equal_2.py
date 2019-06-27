l = list(map(float, input().split(" ")))

while True:
    sum = 0
    equal_counter = 0
    for n in range(len(l)-1):
        if l[n] == l[n+1]:
            sum = l[n] + l[n+1]
            l[n] = sum
            l.remove(l[n+1])
            equal_counter += 1
            break

    if equal_counter == 0:
        break

print(*l)