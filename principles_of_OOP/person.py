class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            print('Name\'s length should not be less than 3 symbols!')
            exit(0)
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print('Age must be positive!')
            exit(0)
        else:
            self.__age = value


class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Person.age.fset(self, value)
        if value > 15:
            print("Child's age must be less than 15!")
            exit(0)
        self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Person.name.fset(self, value)
        self.__name = value



if __name__ == "__main__":
    name = input()
    age = int(input())

    child = Child(name, age)
    print(child)