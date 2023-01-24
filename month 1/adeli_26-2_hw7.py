ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
print(ten)
print(evens)
print(list(map(lambda x: x ** 2, evens)))

def index(ten):
    while True:
        i = (input('введите индекс: '))
        if i == 'exit':
            break
        try:
            i = int(i)
            print(ten[i])
        except:
            print('только цифры от 0 до 9')
print(index(ten))

