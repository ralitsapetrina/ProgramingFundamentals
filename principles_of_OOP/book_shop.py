class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


    def __str__(self):
        return f'Type: Book\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}'

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) < 3:
            print('Title not valid!')
            exit(0)
        else:
            self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        split_author = value.split()
        if len(split_author) >= 2:
            if (split_author[1])[0].isdigit():
                print('Author not valid!')
                exit(0)
            else:
                self.__author = value
        else:
            self.__author = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print('Price not valid!')
            exit(0)
        else:
            self.__price = value


class GoldenEditionBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author, price)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Book.price.fset(self, value)
        value += value * 0.3   # 30% higher price
        self.__price = value

    def __str__(self):
        return f'Type: GoldenEditionBook\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}'


author = input()
title = input()
price = float(input())

book = Book(title=title, author=author, price=price)
golden_edition = GoldenEditionBook(title=title, author=author, price=price)

print(book, '\n')
print(golden_edition)