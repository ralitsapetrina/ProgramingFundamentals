age_dict = {}
salary_dict = {}
position_dict = {}

def print_dicts(com, dict):
    for key,value in dict.items():
        print((f'Name: {key}'
               f'\n{com}: {value}'
               f'\n===================='))

def int_value(value):
    try:
        value = int(value)
    except ValueError:
        return False
    else:
        return True

def float_value(value):
    try:
        value = float(value)
    except ValueError:
        return False
    else:
        return True


while True:
    employee_info = input().split(" -> ")

    if employee_info[0] == "filter base":
        break

    if int_value(employee_info[1]):
        age_dict[employee_info[0]] = employee_info[1]
    elif float_value(employee_info[1]):
        if float(employee_info[1]) % 1 == 0:
            age_dict[employee_info[0]] = employee_info[1]
        else:
            salary_dict[employee_info[0]] = employee_info[1]
    else:
        position_dict[employee_info[0]] = employee_info[1]

command = input()

if command == "Position":
    print_dicts(command, position_dict)
elif command == "Salary":
    print_dicts(command, salary_dict)
elif command == "Age":
    print_dicts(command, age_dict)