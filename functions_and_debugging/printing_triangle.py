def printing_triangle(num):
    for row in range(1, num + 1):
        for col in range(1, row+1):
            print(f'{col}', end=" ")
        print()

    for row2 in range(1, num + 1):
        for col2 in range(1, num-row2+1):
            print(f'{col2}', end=" ")
        print()



if __name__ == "__main__":
    number = int(input())
    printing_triangle(number)