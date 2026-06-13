from modules import Character, battle
from time import sleep


if __name__ == '__main__':
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

    print(
        'Военком: это была шутка. Все равно распределим куда надо. '
        'Садись в машину'
    )

    sleep(2)
    for i in range(0, 4):
        print('...')
        if i == 1:
            sleep(2)
            print('Пассажир: эй, окно откройте! Душно!')
            sleep(2)
            continue
        sleep(2)

    print(
        'Водитель: на выход, приехали!'
    )
    sleep(2)

    print(
        f'{player_name}: ну вот, я снова солдат...'
    )
    sleep(2)

    print('Служивый: эй, молодой! Закурить есть?')
    sleep(2)

    if player.charisma >= 5:
        print(
            f'{player.name}: Серега? Сколько лет, сколько зим!'
            )
        sleep(2)
        serega = Character('Серега')

        print(
            f'{serega.name}: {player.name}, ты что ли? '
            f'Здарова земляк! Иди обниму'
            )
        sleep(2)
    else:
        print(f'{player.name}: а? Что?')
        print(
            'Служивый: сигарету говорю дай! Глухой что ли?\n'
        )
        sleep(2)

        serega = Character('Серега')

        battle(player, serega)

# TODO 1.ПЕРЕПИСАТЬ ПРИСОВЕНИЕ ХАРАКТЕРИСТИК КЛАССУ
# КАЖДАЯ ХАРАКТЕРИСТИКА ПО ДЕФЛТУ = NONE, ЕСЛИ NONE ТО РАНДОМИМ,
# ЭТО НУЖНО ДЛЯ СЮЖЕТНЫХ МОМЕНТОВ, И ДЛЯ ВАЖНЫХ ЮНИТОВ

# 2. СОЗДАТЬ ПОДКЛАСС ВРАГА, И СОЗДАТЬ НЕСКОЛЬКО ТИПОВ ВРАГОВ
# У КАЖДОГО ТИПА ВРАГА ХАРАКТЕРИСТИКИ РАНДОМЯТСЯ В ОПРЕДЕЛЕННОМ ДИАПЗАЗОНЕ
# НАПРИМЕР АЛКАШ: АТАКА В ПЕРЕДАЛХ 1-3, ДЕСАНТ 5-8 И ТД. ТО ЕСТЬ В ЗАВИСИМОСТИ
# ОТ ТИПА ЭНЕМИ ВЫБИРАЕТСЯ ДИАПАЗОН РАНДОМА
