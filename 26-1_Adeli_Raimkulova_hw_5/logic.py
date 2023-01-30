import random
from decouple import config


def start():
    while True:
        die = random.randint(1, 30)
        start_game = (int(input('Новая ставка - 1\nЗавершить игру - 2\nПродолжить игру - 3\nВвод:')))
        startmoney = config("MY_MONEY", cast=int)
        if start_game == 1:
            your_bid = int(input(f'Ваша ставка:'))
            bet = int(input('Выберите число от 1 до 30:'))
            if bet == die:
                new_ball = startmoney + your_bid * 2
                print(f'Верный выбор! Ваша ставка была удвоена!\nВаш баланс: {new_ball}')
            elif bet != die:
                new_ball = startmoney - your_bid
                print(f'К сожалению вы потеряли ставку\nВаш баланс: {new_ball}')
        elif start_game == 3:
            your_bid = int(input(f'Ваша ставка:'))
            bet = int(input('Выберите число от 1 до 30:'))
            if bet == die:
                new_ball = new_ball + your_bid * 2
                print(f'Вам везет! Ваша ставка была удвоена!\nВаш баланс: {new_ball}')
            elif bet != die:
                new_ball = new_ball - your_bid
                print(f'В этот раз удача не на вашей стороне\nВаш баланс: {new_ball}')
        elif start_game == 2:
            print(f'Ваш баланс:{new_ball}\nДо встречи!')
            break

