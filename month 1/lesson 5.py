# Структуры данных: словари, множества
# {key: value}
# dict - словарь
# set - множество

# from random import choice
# from time import sleep
#
# students = [1, 2, 8, 11, 14, 17, 3]
# answers = {}
#
# while len(students) != 0:
#     print(students)
#     student_id = choice(students)
#     name = input(f'имя студента под номером {student_id}: ').title()
#     timer = 25
#     while timer != 0:
#         print(timer)
#         sleep(1)
#         timer -= 1
#     rate = int(input(f'оценка для {name}: '))
#     answers[name] = rate
#     students.remove(student_id)
#
# for name, rate in answers.items():
#     print(f'{name}: {rate}')
#
# print(sum(answers.values()) / len(answers))


# plov = {"рис", "мясо", "морковь"}
# manty = {"тесто", "мясо", "лук"}
#
# print(plov.intersection(manty))
# print(plov & manty)
#
# print(plov.difference(manty))
# print(plov - manty)
#
# print(plov.union(manty))
# print(plov | manty)
#
# print(plov.symmetric_difference(manty))
# print(plov ^ manty)
#
# print(help(set))
# print(dir(set))
#
#
# numbers = {1, 2, 3, 2, 1, 3, 4}
# numbers2 = [1, 2, 3, 2, 1, 3, 4]
#
# numbers.add(5)
# numbers.remove(4)
# numbers.update([2, 4, 6])
#
# print(numbers)
# print(numbers2)
#
#
# # print(type(numbers))
#
#
# # regions = ['chuy', 'osh', 'batken', 'talas', 'y-k', 'naryn', 'jalal-abad']
# # data = {i: int(input(f'введите температуру в {i}')) for i in regions}
# # print(sum(data.values()) / len(data)) сумма значений
#
#
# # numbers = [i for i in range(1, 6)]
# # numbers2 = {i: i*i for i in numbers}
# # print(numbers, numbers2, sep='\n')
#
#
# # new = dict(name='azamat', age=19, country='kg')
# # new = dict([[1, 'one'], [2, 'two']])
# # new = dict(enumerate('python')) ##разобъет слово по буквам/ индекс как ключ
# # print(new)
#
student = {
    'name': 'Johny',
    'age': 20,
}

print(student['name'])

"""add"""
student['weight'] = 65
student['hobby'] = ['chess', 'football', 'english']
# student.update(new)
student['hobby'].append('boxing')

"""edit"""
student['age'] += 1
student['weight'] = 70
student['hobby'][0] = 'programming'

"""delete"""
del student['hobby'][-1]
deleted = student.pop('weight')
# print(deleted)

#
#


###Чтобы был красивый списочек, напиши так
# for i in student:
#     print(f'{i}: {student[i]}')

# for key, value in student.items():
#     print(f'{key} => {value}')

# print(student.keys()) ##показывает только ключт
# print(student.values()) ##показывает только значения
# print(student.items()) ##делит по парам колючи и значения в кортеже

###чтобы не высвечивалась страшная строка ошибки
# print(student['nam'])
# print(student.get('name', 'нет такого ключа'))


# print(type(student))


