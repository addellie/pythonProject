import re

with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
    content = file.read()

while True:
    choise = (int(input('Выберите нужную опцию:\n1.Считать имена и фамилии\n'
                        '2.Считать все емайлы\n3.Считать названия файлов\n'
                        '4.Считать цвета\n5.Выход\nВвод:')))
    if choise == 1:
        with open('names.txt', 'a') as file:
            names = re.findall(r'[A-Z][a-z]+\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?', content)
            file.write(f'{names}')
    elif choise == 2:
        with open('email.txt', 'a') as file:
            email = re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+', content)
            file.write(f'{email}')

    elif choise == 3:
        with open('site.txt', 'a') as file:
            site = re.findall(r'[A-Z][a-zA-Z]+\.[a-z0-9]+', content)
            file.write(f'{site}')

    elif choise == 4:
        with open('colour.txt', 'a') as file:
            colour = re.findall(r'#[0-9A-Fa-f]{6}', content)
            file.write(f'{colour}')
    elif choise == 5:
        print('exit...')
        break



