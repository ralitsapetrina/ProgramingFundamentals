import re


def check_signs(w):
    is_sign = False
    for letter in w:
        if ord(letter) >= 32 and ord(letter) <= 64:
            is_sign = True
    return is_sign


list_string = input()

list = re.split("[\,\;\:\.\!\(\)\"\'\\\/\[\]\ ]+",list_string)

lowercase = []
uppercase = []
mixedcase = []

for word in list:
    if not word:
        continue

    if word.islower():
        if check_signs(word):
            mixedcase.append(word)
        else:
            lowercase.append(word)
    elif word.isupper():
        if check_signs(word):
            mixedcase.append(word)
        else:
            uppercase.append(word)
    else:
        mixedcase.append(word)

print(f'Lower-case:', ', '.join(lowercase))
print(f'Mixed-case:', ', '.join(mixedcase))
print(f'Upper-case:', ', '.join(uppercase))