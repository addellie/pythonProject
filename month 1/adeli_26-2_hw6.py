def first_word(word = 'Hello World'):
    if type(word) != str:
        return False
    return word.split()[0]
print(first_word())


def average(number, *args):
    return (round(sum(args) / len(args)))
print(average(1, 10, 22, 33 , 45, 45, 56,))


def password_security(password):
    if len(password) >= 6 and not password.isnumeric() and not password.isalpha(): ##and not значит не обязательно
        return True
    else:
        return False
print(password_security(input('password:')))

