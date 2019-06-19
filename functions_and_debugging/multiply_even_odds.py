def mult_nums(num):
    result_even = 0
    result_odd = 0
    while num > 0:
        last_dig = num % 10
        if last_dig % 2 == 0:
            result_even += last_dig
        else:
            result_odd += last_dig
        num = num // 10
    return result_even * result_odd


if __name__ == "__main__":
    number = int(input())
    print(mult_nums(abs(number)))