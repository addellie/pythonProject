while True:
    word = input('Введите слово:').lower()
    if word == 'exit':
        print('exit...')
        break
    else:
        vowel = 'aeiouyуеёаоэяиюы'
        consonant = 'bcdfghjklmnpqrstvwxzбвгджзклмнпрстфхцчшщй'
        a = 0
        b = 0
        print('количество букв:', len(word))
    for i in word:
        if i in vowel:
            a += 1
        elif i in consonant:
            b += 1

    percent_a = round(a / len(word) * 100, 2)
    percent_b = round(b / len(word) * 100, 2)
    print('согласных:', int(b))
    print('гласных:', int(a))
    print(f'гласные/согласные: {percent_a}%/{percent_b}%')

