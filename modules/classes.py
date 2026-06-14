from random import randint


class Character:
    """Класс игрового персонажа"""

    # Присвоение характеристик персонажу
    def __init__(
        self,
        name,
        hp=None,
        attack=None,
        defense=None,
        charisma=None,
    ):
        self.name = name
        self.hp = randint(5, 10) if hp is None else hp
        self.attack = randint(5, 10) if attack is None else attack
        self.defense = randint(5, 10) if defense is None else defense
        self.charisma = randint(1, 10) if charisma is None else charisma

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
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

class Monster:
    """Класс игровых монстров"""

    def __init__(self, name):
        self.name = name
        self.hp = None
        self.attack = None
        self.defense = None