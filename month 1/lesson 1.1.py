## типы данных
# #str - string = строка
# #int - integer= целое
# #float - floating = дробное
#print - функция (оператор)

name = 'Adeli'
surname = 'Raimkuova'
print("hello world")
print('hello', name, surname)
print('Hi', name, surname)
print('hello' + name + surname)
print('hello {} {}'.format (name, surname))
print(f'hello {name} {surname}')

#format - метод,обозначается в фигурных скобках (в2) или за ковычками после точки (в1). составление строки
# на основе каких-либо данных
# age = 19
# name = 'adeli'
# # print('Возраст {0} - {1} лет.'.format(name, age))
# print(f'hallo {name} are you {age} year?')

year = int(input('i was born in'))
current_year = 2022
print(f'hello! are you {current_year - year} years old?')

# #десятичное число (.) с точностью в 3 знака для плавающих, в () само чсило. тут одна шестая
# print('{0:.3}'.format(1/6))
# #заполнить подчеркиваниями (_) с центровкой текста (^) по ширине 11
# print('{0:_^11}'.format('hello'))
# #по ключевым словам
# print('{name} написал {book}'.format( name = 'adeli', book = 'lana del ray'))

print('{0:.3}'.format(1/6))
print('{0:-^12}'.format('love'))
print('{name1} fell in love with {name2}'.format( name1 = 'Avrora', name2 = 'Filip'))

# # переменные и константы, где переменные это number а константа это 6. (=)-оператор присваивания
# number = 6
# print(number)
# number = number + 5
# print(number)
#
# d = '''Это многострочная строка.
# Это вторая ее строка'''
# print(d)
#
# #(;) обозначает конец логической строки. но лучше печатать в каждой физической строке как в варианте l,
# # так проще читать код
# l = 3
# print(l)
# k = 8; print(k);

# # (/) - явное объединение строк
# s = 'hi me name is Lana. \
# and i am 19 years old.'
# print(s)

#опреаторы и операнды
#2+3 где 2 и 3 это операнды а (+) оператор
# + сложение
# - вычитание
# * умножение
# ** возведение в степень
# / деление
# // целочисленное деление
# % деление по модулю
# << свдвиг влево
# >> сдвиг вправо
# & побитовое И
# | побитовое ИЛИ
# ^ побитовое Исключительно или
# ~ побитовое НЕ = (х+1)
# < меньше
# > больше
# <= меньше
# >= больше или равно
# == равно
# != не равно

# lenght = 4
# breadth = 7
# area = lenght * breadth
# print('площадь равна', area)
# print('периметр равен', 2 * (lenght + breadth))

#оператор if = блок если
#input() = функция. запрос от пользователя
number = 45
guess = int(input('введите целое число: '))
if guess == number:
    print('вы угадали')# начало нового блока
    print('(хотя и не выйграли никакого приза)')# конец нового блока
#оператор elif = блок
#оператор else = блок иначе
elif guess < number:
    print('Нет, загаданное число немного больше этого.')
else:
    print('нет, загаданное число немного меньше этого.') #чтобы попасть сюда, guess должно быть больше чем number
    print('завершено')#Это последнее выражение выполняется всегда после выполнения опретарора если

# sum_ages = 17 + 18 + 25 + 19 + 20 + 17 + 19 + 16 + 19 + 19 + 18 + 28
# amount_students = 12
# average = sum_ages / amount_students
# average = round(average)
# print(average)

#встроенные функции roud, ptint, int, float, input,
#fotmat метод