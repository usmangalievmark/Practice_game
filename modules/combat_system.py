from time import sleep


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
