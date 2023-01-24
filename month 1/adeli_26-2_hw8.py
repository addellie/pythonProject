# print('Загадайте число от 0 до 100')
# number1, number2 = 1, 100
# count = 0
# while True:
#     x = (number1 + number2) // 2
#     print('Твое число больше, меньше или равно', x, '?')
#     count += 1
#     try:
#         my_number = int(input('1 - больше, 2 - меньше, 3 - равно:'))
#         if my_number == 3:
#             print(f'Ура! Ура! Я угадал с {count} раза. Твое число: {x}.')
#             with open('results.txt', 'a') as file:
#                 file.write( f'Загаданное число {x}\n'
#                             f'Количество попыток {count}\n')
#             break
#         elif my_number == 1:
#             number1 = x
#         elif my_number == 2:
#             number2 = x
#     except ValueError:
#         print('Вы можете ввести цифры от 1 до 3 чтобы выбрать соответствующий ответ')



