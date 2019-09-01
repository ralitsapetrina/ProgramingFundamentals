from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def __init__(self, id: str, os: str, price: float):
        self.id = id
        self.os = os
        self.price = price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not value.isalpha() or len(value) < 8:
            raise Exception('Invalid id!')
        else:
            self.__id = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception('Invalid price!')
        else:
            self.__price = value

    def print_item(self):
        return f'Item id: {self.id}\nOperating system: {self.os}\nPrice: {self.price}'

class Phone(Item):
    @abstractmethod
    def __init__(self, id, os, price):
        Item.__init__(self, id, os, price)

    def make_call(self):
        print('Making call...')

    def receive_call(self):
        print('Receiving a call!')

    def send_message(self):
        print('Sending message...')

    def receive_message(self):
        print('Receiving a message!')

class Tablet(Item):
    def __init__(self, id, os, price):
        Item.__init__(self, id, os, price)

    def stream_movie(self):
        print('Streaming movie...')

class CellPhone(Phone):
    def __init__(self, id, os, price):
        Phone.__init__(self, id, os, price)

class SmartPhone(Phone):
    def __init__(self, id, os, price, apps: list):
        Phone.__init__(self, id, os, price)
        self.apps = apps

    def browse_internet(self):
        print('Browsing...')

    def print_item(self):
        return f'Item id: {self.id}\nOperating system: {self.os}\nPrice: {self.price}\nApplications: {", ".join(self.apps)}'

    @property
    def apps(self):
        return self.__apps

    @apps.setter
    def apps(self, value):
        if len(value) < 5:
            raise Exception('Invalid number of applications!')
        else:
            self.__apps = value

items_dict = {'SmartPhone': [], 'CellPhone': [], 'Tablet': []}

def test_item(command_list, items_dict):
    id = command_list[1]
    functionality = command_list[2]
    found = False
    for search_item in items_dict.values():
        for one_item in search_item:
            if id == one_item.id:
                if functionality in dir(one_item):
                    format = f'one_item.{functionality}()'
                    eval(format)
                    found = True
    if not found:
        print('Invalid request has been made!')

def report_item(command_list, items_dict):
    kind = command_list[1]
    if kind in items_dict.keys():
        for item in items_dict.get(kind):
            print(item.print_item())
    else:
        print('Invalid request has been made!')


while True:
    command = input()
    if command == 'end':
        break
    try:
        type = command.split('(')[0]
        new_obect = eval(command)
        items_dict.get(type).append(new_obect)
    except Exception as ex:
        print(ex)

while True:
    command_list = input().split()
    if command_list[0] == 'end':
        exit(0)
    if command_list[0] == 'test':
        test_item(command_list, items_dict)
    elif command_list[0] == 'report':
        report_item(command_list, items_dict)

