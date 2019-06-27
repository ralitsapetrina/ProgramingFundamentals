list = list(input().split(" "))

def rotate(l):
    return l[-1:] + l[:-1]

print(*rotate(list))