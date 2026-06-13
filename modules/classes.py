from random import randint, choice
from time import sleep


class Character:
    """Класс игрового персонажа"""

    # Список игровых классов.
    percs = ['Штурмовик', 'Снайпер', 'Оператор БПЛА', 'ВПшник', 'Копач']

    def __init__(self, name):
        self.name = name
        self.perc = choice(Character.percs)
        self.hp = randint(5, 10)
        self.attack = randint(5, 10)
        self.defense = randint(5, 10)
        self.charisma = randint(1, 10)

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Специальность: {self.perc}\n'
            f'Здоровье: {self.hp}\n'
            f'Урон: {self.attack}\n'
            f'Защита: {self.defense}\n'
            f'Харизма: {self.charisma}'
        )

    # Функция для нанесения урона.
    def basic_attack(self, opponent):
        damage = max(self.attack - opponent.defense, 1)
        opponent.hp -= damage
        opponent.hp = max(opponent.hp, 0)
        print(
            f'{opponent.name} получает {damage} урона. '
            f'Остаток здоровья: {opponent.hp}'
        )


# Функция имитирует битву между игроков и противником.
def battle(player, opponent):
    print(f'{player.name} против {opponent.name}')
    while opponent.hp > 0 and player.hp > 0:
        player.basic_attack(opponent)
        if opponent.hp <= 0:
            print(f'{player.name} победил')
            break
        sleep(1)
        opponent.basic_attack(player)
        if player.hp <= 0:
            print(f'{opponent.name} победил')
            break
        sleep(1)
