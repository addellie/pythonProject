print('Пожалуйста, введите ниже данные температуры воздуха')
a = int(input('Ошская область:'))
b = int(input('Чуйская область:'))
c = int(input('Иссык-Кульская область:'))
d = int(input('Баткенская область:'))
e = int(input('Джалал-Абадская область:'))
f = int(input('Нарынская область:'))
g = int(input('Таласская область:'))
sum_number = a + b + c + d + e + f + g #сумма
num_of_areas = 7 #число областей
average_temperature = sum_number / num_of_areas #средний показатель
average_temperature = round(average_temperature, 1)
print(f'Средний показатель температуры воздуха в Кыргызстане на сегодня {average_temperature} °C')

# int - переводит строку в число