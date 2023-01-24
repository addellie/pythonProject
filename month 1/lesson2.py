#логические типы данных,условные конструкции и операторы
# bool = boolean (логический тип данных)
# or, and, not (логический оператор)
# ==, !=, <, >, <=, >=, >< (оператор сравнения)
# +=, -=,*=, /= (оператор назначения)
# #[start:stop:step] схема срезов
# #[]- индекс каждой буквы. индексация. работает и в обратную сторону [-1]==я
# #sep='\n' == разделение и перенос на новую строку

# in/ not in (оператор принадлежности) проверка последовательности в объекте
# возвращает true если x in y или x not in y

# # bool - boolean логический тип данных (принимает два значения True and False и является подклассом int)
# #True = 1, False = 0
# print(type(True)) #bool
# print(True+4)
# print(False*8)
# print(bool(1.5))

# print(word.index('A')) #запрашивает индекс буквы
# print(word.isalpha()) #возвращает True если в str все символы = буквенные
# print(word.isnumeric()) #возвращает True если в str все символы = числа
# print(word.startswith('a')) #слово начинается с буквы...
# print(word.endswith('к')) #слово закончилась буквой
# word = 'frustraiting'
# print(len(word)) #количество элементов объекта
# mylist = ['apple', 'banana', 'cherry']
# print(len(mylist))
# string = 'spring'
# print(len(string))

# time = 'evening'
# if time == 'morning':
#    print('good morning')
# elif time == 'day':
#    print('good afternoon')
# elif time =='evening':
#    print('good evening')
# else: #работает если не найден подходящий вариант
#    print('hello')

# time = 'утро'
# if time == 'morning' or time == 'утро':
#    print('good morning')

# #если в коде много if, то они не связаны

# # операторы сравнения
# print(10 == 12-2)
# print(type(20 == 12-2))
# print(2 != 4)
# print(2 > 6)
# print(2 < 6)
# print(2 <= 5)
# print(2 >= 6)

# # or достаточно одного верного ответа (логический опер)
# print(2 < 5 or 2 == 5)

# # and (логический опер)
# print(2 > 1 and 3 < 5)
# print(2 > 1 and 3 < 2)
# print( 1 < 2 > 3) #<> для краткого решения примера выше

# a = 10
# a += 6
# b = a + 10
# print(a, b)

# not (логический опер)
# print(not False)

# #[start:stop:step] схема срезов
# word = 'гидроэлектростанция'
# print(word[0])
# []- индекс каждой буквы. индексация. работает и в обратную сторону [-1]==я
# print(word[0:5]); print(word[:5])
# print(word[0:19:2])
# print(word[::-1])
# new = word[:5]
# print(word)
# print(new)
# electro = word[5:12]
# print(electro)
# print(word, new, electro, sep='\n')
#sep='\n' == разделение и перенос на новую строку
# station = word[12:19] #[:19]
# print(station)
# print(new, electro, station)
# print(new+electro+station)
# print(2*word)
# word2 = "32455668764"
# print(len('word2'))

# password1 = input('введите пароль')
# password2 = input('введите пароль')
# if password1 == password2:
#    print('ok')
# else:
#     print('error')

# password = input('Введите пароль:')
# if len(password) >= 6 and password.isnumeric():
#     print ('Данный пароль верен')
# else:
#     print ('Пароль должен состоять только из цифер и содержать 6 знаков')

# print(bool(0))
# print(bool(1.0))
# priny(bool('123'))

