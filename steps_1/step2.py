# Name Convention va Name Mangling


class Dog:
    def __init__(self, name):
        self.__name = name  # private attribute

    def __method(self):  # private method
        print(self.__name)


if __name__ == "__main__":
    dog = Dog(name='Buldog')
    print(vars(dog))
    print(vars(Dog))
    print(dog.__weakref__)
    print(dog.__dict__)  # API ni ko'rish
    print(dog.__dir__())  # to'liq imkoniyatini ko'rish
    print(dog._Dog__name)  # private attribute ni ko'rish
    dog._Dog__method()  # private method ni ko'rish
