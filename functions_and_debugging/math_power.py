def math_power(num, pow):
    result = num ** pow
    return result


if __name__ == "__main__":
    number = float(input())
    power = float(input())
    print(math_power(number, power))