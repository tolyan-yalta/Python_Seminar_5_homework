# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# 28 * 72 = 2016
# 28 * 71 = 1988
# 28 * 70 = 1960
# 2021 - 1960 = 61
# Для ускорения игры можно сократить начальное число на 1960, будет 2021 - 1960 = 61
initial_number = result = 61
# initial_number = result = 2021

def is_int(value):  # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

import random

print('Какой вариант игры Вы хотите выбрать?')
print('Если человек против человека, то введите "0"')
print('Если против простого бота, то введите "1"')
print('Если против интелектуального бота, то введите "2"')

variant = input('-->  ')

while not is_int(variant) or (int(variant) != 0 and int(variant) != 1 and int(variant) != 2):
    if not is_int(variant):
        variant = input('Это вообше не число, введите 0, 1 или 2  -->  ')
        continue
    elif (int(variant) != 0 and int(variant) != 1 and int(variant) != 2):
        variant = input('Нужно выбрать вариант игры, введите 0, 1 или 2  -->  ')

if variant == '0':
    print('Давайте определим кто будет ходить первый и кинем кубик')
    print('Усли выпадет 1, 2, 3 то первым ходит игрок А')
    print('Если выпадет 4, 5, 6 то первым ходит игрок Б')
    input('Бросайте кубик, нажмите Enter')
else:
    print('Давайте определим кто будет ходить первый и кинем кубик')
    print('Усли выпадет 1, 2, 3 то первым ходите Вы')
    print('Если выпадет 4, 5, 6 то первым хожу я, кстати меня зовут Терминатор :)')
    input('Бросайте кубик, нажмите Enter')

first_step = random.randint(1, 6)
print(f'Выпало {first_step}\n')

def game_man_to_man_variant_1(result):
    print(f'Начинает игрок Б, в наличии {result} конфет')
    while result > 0:
        if result > 28:
            print(f'Осталось {result} конфет')
            number_gamer = input('Конфеты берет игрок Б, возьмите конфеты но не более 28 ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or int(number_gamer) > 28:
                if not is_int(number_gamer):
                    number_gamer = input('Это вообше не число, возьмите конфеты, но не более 28 ')
                elif int(number_gamer) < 0 or int(number_gamer) > 28:
                    number_gamer = input('Нет, нельзя вообще не брать конфеты или взять больше 28, возьмите конфеты ')
            result -= int(number_gamer)
        else:
            print(f'Осталось {result} конфет')
            number_gamer = input(f'Конфеты берет игрок Б, возьмите конфеты ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or  int(number_gamer) > result:
                if not is_int(number_gamer):
                    number_gamer = input(f'Это вообше не число, возьмите конфеты, осталось {result} конфет')
                elif int(number_gamer) < 0 or  int(number_gamer) > result:
                    number_gamer = input(f'Нет, нельзя вообще не брать конфеты или взять больше чем осталось, осталось {result} конфет, возьмите конфеты ')
            result -= int(number_gamer)
            if result == 0:
                print('Победил игрок Б, поздравляем, спасибо за игру')
                break
        if result > 28:
            print(f'Осталось {result} конфет')
            number_gamer = input('Конфеты берет игрок А, возьмите конфеты но не более 28 ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or int(number_gamer) > 28:
                if not is_int(number_gamer):
                    number_gamer = input('Это вообше не число, возьмите конфеты, но не более 28 ')
                elif int(number_gamer) < 0 or int(number_gamer) > 28:
                    number_gamer = input('Нет, нельзя вообще не брать конфеты или взять больше 28, возьмите конфеты ')
            result -= int(number_gamer)
        else:
            print(f'Осталось {result} конфет')
            number_gamer = input(f'Конфеты берет игрок А, возьмите конфеты ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or  int(number_gamer) > result:
                if not is_int(number_gamer):
                    number_gamer = input(f'Это вообше не число, возьмите конфеты, осталось {result} конфет')
                elif int(number_gamer) < 0 or  int(number_gamer) > result:
                    number_gamer = input(f'Нет, нельзя вообще не брать конфеты или взять больше чем осталось, осталось {result} конфет, возьмите конфеты ')
            result -= int(number_gamer)
            if result == 0:
                print('Победил игрок А, поздравляем, спасибо за игру')

def game_man_to_man_variant_2(result):
    print(f'Начинает игрок А, в наличии {result} конфет')
    while result > 0:
        if result > 28:
            print(f'Осталось {result} конфет')
            number_gamer = input('Конфеты берет игрок А, возьмите конфеты но не более 28 ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or int(number_gamer) > 28:
                if not is_int(number_gamer):
                    number_gamer = input('Это вообше не число, возьмите конфеты, но не более 28 ')
                elif int(number_gamer) < 0 or int(number_gamer) > 28:
                    number_gamer = input('Нет, нельзя вообще не брать конфеты или взять больше 28, возьмите конфеты ')
            result -= int(number_gamer)
        else:
            print(f'Осталось {result} конфет')
            number_gamer = input(f'Конфеты берет игрок А, возьмите конфеты ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or  int(number_gamer) > result:
                if not is_int(number_gamer):
                    number_gamer = input(f'Это вообше не число, возьмите конфеты, осталось {result} конфет')
                elif int(number_gamer) < 0 or  int(number_gamer) > result:
                    number_gamer = input(f'Нет, нельзя вообще не брать конфеты или взять больше чем осталось, осталось {result} конфет, возьмите конфеты ')
            result -= int(number_gamer)
            if result == 0:
                print('Победил игрок А, поздравляем, спасибо за игру')
                break
        if result > 28:
            print(f'Осталось {result} конфет')
            number_gamer = input('Конфеты берет игрок Б, возьмите конфеты но не более 28 ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or int(number_gamer) > 28:
                if not is_int(number_gamer):
                    number_gamer = input('Это вообше не число, возьмите конфеты, но не более 28 ')
                elif int(number_gamer) < 0 or int(number_gamer) > 28:
                    number_gamer = input('Нет, нельзя вообще не брать конфеты или взять больше 28, возьмите конфеты ')
            result -= int(number_gamer)
        else:
            print(f'Осталось {result} конфет')
            number_gamer = input(f'Конфеты берет игрок Б, возьмите конфеты ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or  int(number_gamer) > result:
                if not is_int(number_gamer):
                    number_gamer = input(f'Это вообше не число, возьмите конфеты, осталось {result} конфет')
                elif int(number_gamer) < 0 or  int(number_gamer) > result:
                    number_gamer = input(f'Нет, нельзя вообще не брать конфеты или взять больше чем осталось, осталось {result} конфет, возьмите конфеты ')
            result -= int(number_gamer)
            if result == 0:
                print('Победил игрок Б, поздравляем, спасибо за игру')


def find_number_bot(value):
    number_bot = random.randint(1, value)
    return number_bot

def game_to_bot_variant_1(result):
    print(f'Что же, я начинаю, я бот и зовут меня Терминатор, в наличии {result} конфет')
    while result > 0:
        if result > 28:
            number_bot = find_number_bot(28)
        else:
            number_bot = find_number_bot(result)
        print(f'я возьму {number_bot} конфет')
        result -= number_bot
        if result == 0:
            print('Ура! Победил бот Терминатор. Ха-ха-ха, Терминатор непобедим!')
            break
        if result > 28:
            print(f'Осталось {result} конфет')
            number_gamer = input('Возьмите конфеты, но не более 28 ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or int(number_gamer) > 28:
                if not is_int(number_gamer):
                    number_gamer = input('Это вообше не число, возьмите конфеты, но не более 28 ')
                elif int(number_gamer) < 0 or int(number_gamer) > 28:
                    number_gamer = input('Нет, нельзя вообще не брать конфеты или взять больше 28, возьмите конфеты ')
            result -= int(number_gamer)
        else:
            print(f'Осталось {result} конфет')
            number_gamer = input(f'Возьмите конфеты ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or  int(number_gamer) > result:
                if not is_int(number_gamer):
                    number_gamer = input(f'Это вообше не число, возьмите конфеты, осталось {result} конфет')
                elif int(number_gamer) < 0 or  int(number_gamer) > result:
                    number_gamer = input(f'Нет, нельзя вообще не брать конфеты или взять больше чем осталось, осталось {result} конфет, возьмите конфеты ')
            result -= int(number_gamer)
            if result == 0:
                print('Ну что же, Вы победили, спасибо за игру')

def game_to_bot_variant_2(result):
    print(f'Привет, я бот и зовут меня Терминатор. Что же, начинайте в наличии {result} конфет')
    while result > 0:
        if result > 28:
            print(f'Осталось {result} конфет')
            number_gamer = input('Возьмите конфеты, но не более 28 ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or int(number_gamer) > 28:
                if not is_int(number_gamer):
                    number_gamer = input('Это вообше не число, возьмите конфеты, но не более 28 ')
                elif int(number_gamer) < 0 or int(number_gamer) > 28:
                    number_gamer = input('Нет, нельзя вообще не брать конфеты или взять больше 28, возьмите конфеты ')
            result -= int(number_gamer)
        else:
            print(f'Осталось {result} конфет')
            number_gamer = input(f'Возьмите конфеты ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or  int(number_gamer) > result:
                if not is_int(number_gamer):
                    number_gamer = input(f'Это вообше не число, возьмите конфеты, осталось {result} конфет')
                elif int(number_gamer) < 0 or  int(number_gamer) > result:
                    number_gamer = input(f'Нет, нельзя вообще не брать конфеты или взять больше чем осталось, осталось {result} конфет, возьмите конфеты ')
            result -= int(number_gamer)
            if result == 0:
                print('Ну что же, Вы победили, спасибо за игру')
                break
        if result > 28:
            number_bot = find_number_bot(28)
        else:
            number_bot = find_number_bot(result)
        print(f'я возьму {number_bot} конфет')
        result -= number_bot
        if result == 0:
            print('Ура! Победил бот Терминатор. Ха-ха-ха, Терминатор непобедим!')


def find_number_smart_bot(value):
    if value > 28:
        # value = (value - 29) % 28
        return (value - 29) % 28
    else:
        return value

def game_to_smart_bot_variant_1(result):
    print(f'Что же, я начинаю, я бот и зовут меня Терминатор, в наличии {result} конфет')
    while result > 0:
        number_bot = find_number_smart_bot(result)
        print(f'я возьму {number_bot} конфет')
        result -= number_bot
        if result == 0:
            print('Ура! Победил бот Терминатор. Ха-ха-ха, Терминатор непобедим!')
            break
        if result > 28:
            print(f'Осталось {result} конфет')
            number_gamer = input('Возьмите конфеты, но не более 28 ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or int(number_gamer) > 28:
                if not is_int(number_gamer):
                    number_gamer = input('Это вообше не число, возьмите конфеты, но не более 28 ')
                elif int(number_gamer) < 0 or int(number_gamer) > 28:
                    number_gamer = input('Нет, нельзя вообще не брать конфеты или взять больше 28, возьмите конфеты ')
            result -= int(number_gamer)
        else:
            print(f'Осталось {result} конфет')
            number_gamer = input(f'Возьмите конфеты ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or  int(number_gamer) > result:
                if not is_int(number_gamer):
                    number_gamer = input(f'Это вообше не число, возьмите конфеты, осталось {result} конфет')
                elif int(number_gamer) < 0 or  int(number_gamer) > result:
                    number_gamer = input(f'Нет, нельзя вообще не брать конфеты или взять больше чем осталось, осталось {result} конфет, возьмите конфеты ')
            result -= int(number_gamer)
            if result == 0:
                print('Ну что же, Вы победили, спасибо за игру')

def game_to_smart_bot_variant_2(result):
    print(f'Привет, я бот и зовут меня Терминатор. Что же, начинайте в наличии {result} конфет')
    while result > 0:
        if result > 28:
            print(f'Осталось {result} конфет')
            number_gamer = input('Возьмите конфеты, но не более 28 ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or int(number_gamer) > 28:
                if not is_int(number_gamer):
                    number_gamer = input('Это вообше не число, возьмите конфеты, но не более 28 ')
                elif int(number_gamer) < 0 or int(number_gamer) > 28:
                    number_gamer = input('Нет, нельзя вообще не брать конфеты или взять больше 28, возьмите конфеты ')
            result -= int(number_gamer)
        else:
            print(f'Осталось {result} конфет')
            number_gamer = input(f'Возьмите конфеты ')
            while not is_int(number_gamer) or int(number_gamer) < 0 or  int(number_gamer) > result:
                if not is_int(number_gamer):
                    number_gamer = input(f'Это вообше не число, возьмите конфеты, осталось {result} конфет')
                elif int(number_gamer) < 0 or  int(number_gamer) > result:
                    number_gamer = input(f'Нет, нельзя вообще не брать конфеты или взять больше чем осталось, осталось {result} конфет, возьмите конфеты ')
            result -= int(number_gamer)
            if result == 0:
                print('Ну что же, Вы победили, спасибо за игру')
                break
        number_bot = find_number_smart_bot(result)
        print(f'я возьму {number_bot} конфет')
        result -= number_bot
        if result == 0:
            print('Ура! Победил бот Терминатор. Ха-ха-ха, Терминатор непобедим!')

if variant == '0':
    if first_step > 3:
        game_man_to_man_variant_1(result)
    else:
        game_man_to_man_variant_2(result)
elif variant == '1':
    if first_step > 3:
        game_to_bot_variant_1(result)
    else:
        game_to_bot_variant_2(result)
elif variant == '2':
    if first_step > 3:
        game_to_smart_bot_variant_1(result)
    else:
        game_to_smart_bot_variant_2(result)

print('Game over')  
