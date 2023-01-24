data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = [i for i in data_tuple if type(i) == str]
letters.append(True)
letters.reverse()
letters[1] = 'G'
letters[7] = 'C'
numbers = [i for i in data_tuple if type(i) != str]
numbers.remove(True)
numbers.remove(6.13)
numbers.insert(2, 2)
numbers.sort()
numbers = [i**2 for i in numbers]

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)




