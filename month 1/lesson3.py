#циклы: for, while

# WHILE

c = 0

# while True:
#     print('hello', c)
#     c += 1

# while c < 50:
#     print('hello', c)
#     c += 1

# while c < 50:
#     if c == 10:
#         break
#     print('hello', c)
#     c += 1

# while c < 50:
#     c += 1
#     if c == 10:
#         continue # # пропуск оставшегося кода( тут 10) и продолжение цикла
#     print('hello', c)

# while c < 50:
#     c += 1
#     if c % 2 == 0: # # В данном случае игнорируются все четные
#         continue
#     print('hello', c)

# while True:
#     time = input('')
#     if time == 'exit':
#         print('bye')
#         break
#     if time == 'morning':
#        print('good morning')
#     elif time == 'day':
#        print('good afternoon')
#     elif time =='evening':
#        print('good evening')
#     else: #работает если не найден подходящий вариант
#        print('hello')

# rounds = 5
# while rounds > 0: #rounds != 0
#     print(rounds)
#     rounds -= 1

# FOR
#i - iterable, item

word = 'python'
for letter in word: ## для каждой буквы в словк. будет наоборот если[::-1]
    if letter == 'h':
        break #continue
    print(letter)

# for number in range(1, 11):
#     print(number)

# for number in range(1, 11):
#     if number % 2 == 0:
#         print(number)

for i in range(1, 4, ): # как часы, где К это минуты
    for k in range(1, 4):
        print(i, k)

cash = 100
percents = 0.3
years = 5

# for i in range(1, years+1):
#     cash += cash * percents
#     print(f'год: {i} >> {cash}')

# eng ="qwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
#
# while True:
#     word = input ('\nвведите слово:').lower()
#     if word == 'выход':
#         print('exit...')
#         break
#     for i in word:
#         if i in rus:
#             print(eng[rus.index(i)], end='')
#         else:
#             print(rus[eng.index(i)], end='')
#
#




