class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Animal:
    def __init__(self, name, age, address):
        self.__name = name
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError('Value for age must be positive number')
        if isinstance(address, Address):
            self.__address = address
        else:
            raise ValueError('Attribute address must be of data type Address')
        self.__was_born()

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self.__age = new_age
        else:
            raise ValueError('Value for age must be positive number')

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def info(self):
        return f'Name: {self.__name} age: {self.__age} birth year: {self.get_birth_year()}\n' \
               f'Address Info: {self.__address.city}, {self.__address.street} {self.__address.number}'

    def get_birth_year(self):
        return 2023 - self.__age

    def __was_born(self):
        print(f'{self.__name} was born')

    def speak(self):
        raise NotImplementedError('Method speak must be overriden')


class Cat(Animal):
    def __init__(self, name, age, address):
        super(Cat, self).__init__(name, age, address)

    def info(self):
        return f'Cat with ' + super().info()

    def speak(self):
        print('Myayu myau')


class Dog(Animal):
    def __init__(self, name, age, commands, address):
        super(Dog, self).__init__(name, age, address)
        self.__commands = commands

    def speak(self):
        print('Gav gav')

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f'\nCommands: {self.__commands}'


class Fish(Animal):
    def __init__(self, name, age, address):
        super(Fish, self).__init__(name, age, address)

    def speak(self):
        print('Fish says nothing')

some_address = Address('Bishkek', 'Toktogula', 45)
animal = Animal('Animalll', 5, some_address)
animal.set_age(4)
# print(animal.info())
# animal.__was_born()

cat = Cat('Tom', 2, some_address)
# print(cat.info())

dog = Dog('Reks', 1, 'Sit, Run', Address('NY', 'Wall Street', 223))
dog.commands = dog.commands + ', Bark'
# print(dog.info())

fish = Fish('Dori', 3, some_address)

animal_list = [cat, dog, fish]
for animal in animal_list:
    print(animal.info())
    animal.speak()
