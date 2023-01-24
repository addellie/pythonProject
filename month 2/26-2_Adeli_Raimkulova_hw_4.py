import random
from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    STUN = 5
    RESURRECTION = 6
    BOOM = 7
    HACKER = 8
    SHURIKEN = 9



class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            coefficient = random.randint(2, 5)
            boss.health -= self.damage * coefficient
            print(f'Warrior hits critically {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                if hero.health > 0:
                    coefficient = random.randint(1, 5)
                    hero.damage += coefficient
                    print(f'{self.name} increased the attack for {hero.name} by {coefficient} points')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                if hero.health > 0 and self != hero:
                    hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        pass


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.RESURRECTION)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                if hero.health == 0 and self != hero:
                    hero.health += self.health
                    print(f'{self.name} resurrected {hero.name}')
                    self.health = 0
                    self.damage = 0
                    break
        if self.health == 0:
            pass


class Bomber(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOM)

    def apply_super_power(self, boss, heroes):
        if self.health == 0:
            boss.health -= 100
            print(f'{self.name} died and dealt an additional blow of a 100 points')


class Samurai(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SHURIKEN)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            coefficient = random.randint(1, 2)
            if coefficient == 1:
                virus = random.randint(1, 100)
                boss.health -= virus
                print(f'{self.name} threw a shuriken with a virus and caused {virus} damage')
            elif coefficient == 2:
                vaccine = random.randint(1, 100)
                boss.health += vaccine
                print(f'{self.name} threw a shuriken with a vaccine and restored his health by {vaccine} points')


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.HACKER)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            coefficient = random.randint(1, 100)
            random_hero = random.choice(heroes)
            if round_number % 2 == 0 and random_hero.health > 0:
                boss.health -= coefficient
                random_hero.health += coefficient
                print(f"{random_hero.name} add boss's {coefficient} health points")




round_number = 0


def print_statistics(boss, heroes):
    print(f'ROUND {round_number} -------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss('Devil', 1000, 50)
    warrior = Warrior('Axe', 270, 10)
    doc = Medic('Invoker', 250, 5, 15)
    magic = Magic('Dambldor', 280, 15)
    berserk = Berserk('Tigril', 260, 10)
    assistant = Medic('Swan', 290, 5, 5)
    witcher = Witcher('Azazel', 290, 0)
    bomber = Bomber('Bambi', 200, 5)
    samurai = Samurai('Kakashi', 290, 10)
    hacker = Hacker('Bill', 200, 10)

    heroes = [warrior, doc, magic, berserk, assistant, witcher, bomber, samurai, hacker]


    print_statistics(boss, heroes)
    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()

