# print('Чтобы узнать знак зодиака введите день и месяц')
# d = int(input('День'))
# m = int(input('Месяц'))

day_month = input('your bd')
d = int(day_month[:2])
m = int(day_month[3:])

if 31 >= d >= 21 and m == 3 or 1 <= d <= 20 and m == 4:
    print('Овен')
elif 30 >= d >= 21 and m == 4 or 1 <= d <= 20 and m == 5:
    print('Телец')
elif 31 >= d >= 22 and m == 5 or 1<= d <= 21 and m == 6:
    print('Близнецы')
elif 30 >= d >= 22 and m == 6 or 1 <= d <= 22 and m == 7:
    print('Рак')
elif 31 >= d >= 23 and m == 7 or 1 <= d <= 21 and m == 8:
    print('Лев')
elif 31 >= d >= 22 and m == 8 or 1 <= d <= 23 and m == 9:
    print('Дева')
elif 30 >= d >= 24 and m == 9 or 1 <= d <= 23 and m == 10:
    print('Весы')
elif 31 >= d >= 24 and m == 10 or 1 <= d <= 22 and m == 11:
    print('Скорпион')
elif 30 >= d >= 23 and m == 11 or 1 <= d <= 22 and m == 12:
    print('Стрелец')
elif 31 >= d >= 23 and m == 12 or 1 <= d <= 20 and m == 1:
    print('Козерог')
elif 31 >= d >= 21 and m == 1 or 1 <= d <= 19 and m == 2:
    print('Водолей')
elif 29 >= d >= 20 and m == 2 or 1 <= d <= 20 and m == 3:
    print('Рыбы')
else:
    print('Не верный ввод')


#как надо с диапозоном
# if 31 >= day >= 21 and month ....