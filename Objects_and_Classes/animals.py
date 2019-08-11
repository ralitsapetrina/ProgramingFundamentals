class Dog:
    def __init__(self, name, age, num_legs):
        self.name = name
        self.age = age
        self.legs = num_legs

    def talk(self):
        return 'I\'m a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.'

    def show_info(self):
        return f'Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.legs}'

class Cat:
    def __init__(self, name, age, intelligence_quotient):
        self.name = name
        self.age = age
        self.iq = intelligence_quotient

    def talk(self):
        return 'I\'m an Aristocat, and I will now produce an aristocratic sound! Myau Myau.'

    def show_info(self):
        return f'Cat: {self.name}, Age: {self.age}, IQ: {self.iq}'

class Snake:
    def __init__(self, name, age, cruelty_coef):
        self.name = name
        self.age = age
        self.cruel_coef = cruelty_coef

    def talk(self):
        return 'I\'m a Sophistisnake, and I will now produce a sophisticated sound! Honey, I\'m home.'

    def show_info(self):
        return f'Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruel_coef}'

def create_an_animal(data_list, animal):
    return animal(data_list[1], data_list[2], data_list[3])

def print_animals(animal_dict):
    for value in animal_dict.values():
        print(f'{value.show_info()}')


dogs_dict = {}
cats_dict = {}
snakes_dict = {}
animals_dicts_list = [dogs_dict, cats_dict, snakes_dict]

while True:
    command_list = input().split()
    if command_list[0] == 'I\'m':
        break

    if command_list[0] == 'talk':
        for animal in animals_dicts_list:
            if command_list[1] in animal.keys():
                print(animal.get(command_list[1]).talk())
                break
    else:
        if command_list[0] == 'Dog':
            dogs_dict[command_list[1]] = create_an_animal(command_list, Dog)
        elif command_list[0] == 'Cat':
            cats_dict[command_list[1]] = create_an_animal(command_list, Cat)
        elif command_list[0] == 'Snake':
            snakes_dict[command_list[1]] = create_an_animal(command_list, Snake)

print_animals(dogs_dict)
print_animals(cats_dict)
print_animals(snakes_dict)