def greater_int(v1, v2):
    print(max(int(v1), int(v2)))


def greater_string(v1, v2):
    print(max(v1, v2))


def greater_char(v1, v2):
    print(max(v1, v2))


if __name__ == "__main__":
    value_type = input()
    value1 = input()
    value2 = input()
    if value_type == "char":
        greater_char(value1, value2)
    elif value_type == "string":
        greater_string(value1, value2)
    elif value_type == "int":
        greater_int(value1, value2)