# any()
# all()
# lambda, и работа с исключениями
# lambda arguments: expression
# map, filter, sorted

# try:
#     code
# except:
#     message, define smth
# finally:
#     message
#
# raise, assert


# def func(a, b):
#     return a + b
#
# assert func(2, 3) == 5
# assert func(3, 3) == 7, f'неправильно! func(3, 3) должно вернуть {func(3, 3)}'


word = 'python'
while True:
    try:
        i = int(input('введите индекс: '))
        print(word[i])
    except:
        print('только цифры от 0 до 5')


    # except IndexError:
    #     print('неверный индекс!')
    # except ValueError:
    #     print('только цифры')





# from random import choice
# from time import sleep
#
students = [1, 2, 8, 11, 14, 17, 3]
answers = {}

while len(students) != 0:
    print(students)
    student_id = choice(students)
    name = input(f'имя студента под номером {student_id}: ').title()

    if not name.isalpha():
        raise Exception('имя должно состоять только из букв:')

    try:
        rate = int(input(f'оценка для {name}: '))
    except:
        print('только цифры!')
        continue
    answers[name] = rate
    students.remove(student_id)

for name, rate in answers.items():
    print(f'{name}: {rate}')

print(sum(answers.values()) / len(answers))




try:
    print(2 + '2')
except:
    print('неверный тип данных')
finally:
    print('проверка завершена')

print(int('qwe'))
print(a)
print(10/0)


def average(*args):
    return sum(args) / len(args)

result = lambda *args: sum(args) / len(args)
print(result(2, 3, 4))


numbers = list(range(1, 11))
new = sorted(numbers, key=lambda x: x % 2 == 0, reverse=True)

new = tuple(filter(lambda x: x > 5, numbers))
new = [i for i in numbers if i > 4]

new = list(map(str, numbers))
new = [i*2 for i in numbers]

print(f"{numbers=}, \n {new=}")





lambda_func = lambda a, b: a + b

def def_func(a, b):
    return a + b

print(type(lambda_func))
print(type(def_func))

print(lambda_func(2, 3))
print(def_func(2, 3))


def up_letter(word):
    return word.title()


def up_last(word):
    return word[:-1] + word[-1].title()


def show_words(func, words):
    for word in words:
        print(func(word))


words = ['pen', 'book', 'green']
show_words(lambda word: word[:-1] + word[-1].title(), words)

show_words(lambda word: word.title(), words)
show_words(up_letter, words)
show_words(type, words)
show_words(len, words)
