# Basic Approach

# arr_str = input()
# my_dict = {}
#
# for letter in arr_str:
#     key = letter
#     value = arr_str.count(letter)
#     my_dict[key] = value
#
# for key, value in my_dict.items():
#     print(f'{key} -> {value}')


#Dictionary comprehension
arr_str = input()
my_dict = {}

my_dict = {letter: arr_str.count(letter) for letter in arr_str}

for key, value in my_dict.items():
    print(f'{key} -> {value}')
