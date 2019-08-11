class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.sound = ''
        self.produce_sound()

    def produce_sound(self):
        return f'{self.sound}'

    def __str__(self):
        return f'{self.__class__.__name__}\n{self.name} {self.age} {self.gender}\n{self.produce_sound()}'

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise Exception('Invalid input!')
        else:
            self.__age = value


class Dog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)
        self.sound = 'Woof!'


class Frog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)
        self.sound = 'Ribbit'


class Cat(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)
        self.sound = 'Meow meow'


class Kitten(Cat):
    def __init__(self, name, age, gender):
        Cat.__init__(self, name, age, gender)
        self.gender = 'Female'
        self.sound = 'Meow'


class Tomcat(Cat):
    def __init__(self, name, age, gender):
        Cat.__init__(self, name, age, gender)
        self.gender = 'Male'
        self.sound = 'MEOW'


while True:
    command = input()
    if command == 'Beast!':
        break

    name, age, gender = input().split()
    try:
        if command in globals():
            animal_class = globals()[command]
            animal = animal_class(name, int(age), gender)
            print(animal)
        else:
            print('Invalid input!')
    except Exception as e:
        print(str(e))
