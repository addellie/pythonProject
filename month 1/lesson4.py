#структуры данных: списки list, срезы, кортеж tiple
# list - список, в выводе имеет квадратные скобки

# numbers = list(range(1, 6))
# numbers = [i for i in range(1, 6)]
# numbers = [i*3 for i in range(1, 6) if i < 4]
# print(numbers)

words = [False, 34.6, 55, 34.6, 'true', 3, 12, 5, 18]
# words = ['false', 'apple', 'book', 'true', 'geektech']
# new_copy = words.copy()
# new_copy = words.copy
# print(new_copy is words) ##сравнивет по id
# print(new_copy == words) ## сравнивет по содержанию
# print(id(new_copy), id(words))

# new_copy[0] = 555

# print(f'{words=}')
# print(f'{new_copy=}')

# words.reverse() ##задом на перед
# words.sort() ## сортирует по алфавиту
# print(words)


"""удаление"""
# words[4] = words[4].replace('t', '')
# words.remove(34.6) ## уберет первую встречную
# deleted = words.pop(-1) ## уберет индекс -1
# print(deleted)
# del words[1:5] ## удаляет соответсвующие объекты
# words = [i for i in words if words.count(i) < 2] ##
# print(words)


"""изменение"""
# words[3], words[4] = words[4], words[3]
# words[2] = 'frontend'
words[0] /= 2
# words[1:3] = [input('введите слово: ')]
print(words)
"""добавление"""
# words.append(100)
# words.insert(4, 'geektech')
# words.extend(numbers)
# words += numbers

# print(type(words))
# print(type(numbers))

# tuple - кортеж. не изменяем как список, в выводе имеет круглые скобки

# objects = (12, 10)
# objects += (2, 4, 5)
# objects = list(objects) ##образует список из кортежа
# objects.append(123) ##добавить в конце
# objects = tuple(objects) ##образует кортеж из списка
# objects[0] = 23 ##заменна 0го индекса
# print(type(objects))
# print(objects)
