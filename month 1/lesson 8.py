##Работа с файлами
# w - write запись, перезапись
# a - add дозапись
# x - бесконфликтный режим создания файла
# r - read чтение

# file = open('file.txt', 'w')
# file.write('Бишкек, Кыргызстан!')
# file.close() ##надо обязатель закрывать
#
# with open('file.txt', 'a') as file: ##контектный менеджр, автоматически завершающий код. Новая верися верхнего кода
#     file.write('\n2222222222')

# with open('file.txt', 'r') as file:
#     print(file.read())
#     print(file.readline()) ##вызывает строчки по очереди. Если поменять местами с верхней строкой. то он выделит первую строчку файла
#     print(file.readlines())

# from time import sleep
# with open('file.txt', 'r') as file:
#     # start = 0
#     # end = 4
#     # while start < 18:
#     for i in file.readlines():
#         sleep(1)
#         print(i, end='')
        # start += end
        # end += 4

    # print(file.read())
    # print(file.readlines()[3])
    # print(file.readline())


# file = open('file.txt', 'w', encoding='utf-8')
# file.write('123345456')
# file.close()

# with open('new.txt', 'x') as file:
#     file.write('\n222222222')





# from datetime import datetime
# from random import choice, randint
# students = [2, 8, 6, 9, 1, 3, 11]
#
# while len(students) != 0:
#     print(f'ещё в живых: {students}')
#     student_id = choice(students)
#     name = input(f'name: {student_id} ').title()
#     start = datetime.now()
#     first = randint(1, 11)
#     second = randint(10, 300)
#     right_answer = first * second
#     user_answer = int(input(f'сколько будет {first} * {second}'))
#     end = datetime.now() - start
#     if user_answer == right_answer:
#         print(True)
#         with open('answers.txt', 'a') as file:
#             file.write(f'{name} {first} * {second} = {user_answer}'
#                        f' ({right_answer}) {end.seconds} {True}\n')
#     else:
#         print(False)
#         with open('answers.txt', 'a') as file:
#             file.write(f'{name} {first} * {second} = {user_answer}'
#                        f' ({right_answer}) {end.seconds} {False}\n')
#     students.remove(student_id)
#
#
user = {"пользователь", "Шерлок", "пароль", "BakerStreet221"}
print(user['пароль'])
#
#
#