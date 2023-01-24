data = ("O", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = [i for i in data if i.isalpha()]
codes = [i for i in data if i.isnumeric()]

operators = {}
a = 0
b = 0
while a!= len(designations):
    operators[designations[a]] = set([codes[b]])
    a += 1
    b += 1
operators.pop('Fonex')
operators.pop('Katel')
operators['O'].update(['0700', '0500'])
operators['Megacom'].update(['0999', '0555'])
operators['Beeline'].update(['0222', '0777'])
for i in operators:
    print(f'{i} - {operators[i]}')









