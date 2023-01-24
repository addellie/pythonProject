## Функции, аргументы: *args, **kwargs (ключевой аргумент)
## DRY = do not repeat yourself
## def - definition (определение). функция

# def greet(name, surname): ##name - обязательный позиционный параметр if surname = 'unknown' - это не обязательный позиционный параметр
#     print(f'name: {name}, surname:{surname}')

# greet('Adeli', 'Raimkulova')
# greet('Milana','Alinova') ##обязательный позиционный параметр (параметры при создании функции)
# greet(surname = 'Aliyanova', name = 'Maerkul') ##Keyword arguments (именнованные аргументы при прописании функции)

def len1(seq):
    counter = 0
    for i in seq:
         counter += 1
    return(counter)

print(len1('123'))
print(len('123'))



# width = 5
# length = 7
# square_2 = width * length
# print(square_2)
#
def get_area(width: int, length: int) -> int:
    """принимает два значения, ширина и длина.
    Возвращает площадь (целое число)""" #документация выводится через doc
    return width*length

square_2 = get_area(2, 5)
square_hall = get_area(7, 10)
print(square_2, square_hall, sep='\n')
print(get_area.__doc__)
print(help(get_area))

def plus(a, *args): ## позволает неограниченное число аргументов
    print(args)
    return sum(args)

print(plus(10, 15, 30, 50, 11))

def menu(**kwargs):
    return sum(kwargs.values())

print(menu(a=1, b=2))


students_rates = {
    'bogdan' : 4,
    'marsel' : 3,
    'alan' : 5
}

def find_student(name):
    if name in students_rates.keys():
        return True
    return False

def add(name: str, rate: int):
    if name not in students_rates.keys():
        if rate in range(1, 6):
            students_rates[name] = rate
        else:
            print('только от 1 до 5')
    else: print(f'{name} такого имени нет')

def delete(name):
    if name in students_rates.keys():
        del students_rates[name]
    else:
        print(f'{name} there is no name')

def edit(name, new_name):
    if name in students_rates.keys():
        students_rates[new_name] = students_rates.pop(name)

while True:
    print(students_rates)
    command = input(f'1) add\n'
                    f'2) edit\n'
                    f'3) delete\n')
    if command == '1':
        add(name=input('new name:'), rate=int(input('new rate:')))
    elif command == '2':
        edit(name=input('old name'), new_name=input('new name:'))
    elif command == '3':
        delete(name=input('delered name'))
    else:
        print('error bitch')



# width = 7
# length = 15
# square_hall = width * length
# print(square_hall)