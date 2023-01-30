from random import randint

number = 10
list = []
for i in range(number):
    list.append(randint(1, 99))
print(list)

for i in range(number - 1):
    for j in range(number - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]

print(list)
