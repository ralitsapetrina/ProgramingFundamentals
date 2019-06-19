def check_num(num):
    if num > 0:
        print(f"The number {num} is positive.")
    elif num == 0:
        print(f"The number 0 is zero.")
    else:
        print(f'The number {num} is negative.')


if __name__ == "__main__":
    number = int(input())
    check_num(number)