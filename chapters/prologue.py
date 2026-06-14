from modules.classes import Character
from modules.combat_system import battle
from modules.special_functions import game_print
from time import sleep


def prologue():
    print(
        'Военком: здарова бродяга! Ты откуда такой очарованный? '
        'Имя то у тебя есть?'
        )

    player_name = input().strip().capitalize()

    player = Character(player_name)

    print(
        'Военком: мда, фантазия у твоих родителей ни к черту! '
        'Где хочешь служить?'
    )

    player_answer = input().strip().lower()

    if player_answer == 'вдв':
        game_print(
            'Сынок, ты на солнце чтоль перегрелся? Какое тебе вдв? '
            'Садись в машину, десантура'
        )
    else:
        game_print(
            'Военком: это была шутка. Все равно распределим куда надо. '
            'Садись в машину'
        )

    for i in range(0, 4):
        print('...')
        if i == 1:
            sleep(2)
            print('Пассажир: эй, окно откройте! Душно!')
            sleep(2)
            continue
        sleep(2)

    game_print(
        'Водитель: на выход, приехали!'
    )

    game_print(
        f'{player_name}: ну вот, я снова солдат...'
    )

    game_print('Служивый: эй, молодой! Закурить есть?')

    if player.charisma >= 5:
        game_print(
            f'{player.name}: Серега? Сколько лет, сколько зим!'
            )
        serega = Character('Серега')

        game_print(
            f'{serega.name}: {player.name}, ты что ли? '
            f'Здарова земляк! Иди обниму'
            )
    else:
        game_print(
            f'{player.name}: а? Что?'
        )
        print(
            'Служивый: сигарету говорю дай! Глухой что ли?\n'
        )

        serega = Character('Серега', hp=15, attack=5, defense=5)

        battle(player, serega)

    game_print(
        f'{serega.name}: неплохо дерешься для новобранца. '
        'Где служил?'
    )
