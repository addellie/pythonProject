def binary_search(list, item):
    low = 0
    high = len(list) - 1
    i = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        i = i + 1
        print(i)
    return None

from random import randint
my_list = []
for i in range(10):
    my_list.append(randint(1, 50))
my_list.sort()

print(my_list)
print(binary_search(my_list, 22))

