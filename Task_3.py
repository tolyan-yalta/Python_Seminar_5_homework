# Создайте программу для игры в ""Крестики-нолики"".

def is_int(value):  # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

def print_game():
    print(f'-----------------\n  {f[0]}  |  {f[1]}  |  {f[2]} ')
    print(f'-----------------\n  {f[3]}  |  {f[4]}  |  {f[5]} ')
    print(f'-----------------\n  {f[6]}  |  {f[7]}  |  {f[8]} \n-----------------')

def victory(value):
    if f[0] == f[1] == f[2]:
        return True
    elif f[3] == f[4] == f[5]:
        return True
    elif f[6] == f[7] == f[8]:
        return True
    elif f[0] == f[3] == f[6]:
        return True
    elif f[1] == f[4] == f[7]:
        return True
    elif f[2] == f[5] == f[8]:
        return True
    elif f[0] == f[4] == f[8]:
        return True
    elif f[2] == f[4] == f[6]:
        return True
    else:
        return False

def logic_attack(value):
    if value[0] == 2 and value[1] == 2 and value[2] == 0:    # ветка 0
        return 2
    elif value[2] == 2 and value[5] == 2 and value[8] == 0:
        return 8
    elif value[8] == 2 and value[7] == 2 and value[6] == 0:
        return 6
    elif value[6] == 2 and value[3] == 2 and value[0] == 0:
        return 0

    if value[1] == 2 and value[2] == 2 and value[0] == 0:  # ветка 1
        return 0
    elif value[5] == 2 and value[8] == 2 and value[2] == 0:
        return 2
    elif value[7] == 2 and value[6] == 2 and value[8] == 0:
        return 8
    elif value[3] == 2 and value[0] == 2 and value[6] == 0:
        return 6

    if value[0] == 2 and value[2] == 2 and value[1] == 0:  # ветка 2
        return 1
    elif value[2] == 2 and value[8] == 2 and value[5] == 0:
        return 5
    elif value[8] == 2 and value[6] == 2 and value[7] == 0:
        return 7
    elif value[6] == 2 and value[0] == 2 and value[3] == 0:
        return 3

    if value[4] == 2 and value[1] == 2 and value[7] == 0:    # ветка 3
        return 7
    elif value[4] == 2 and value[5] == 2 and value[3] == 0:
        return 3
    elif value[4] == 2 and value[7] == 2 and value[1] == 0:
        return 1
    elif value[4] == 2 and value[3] == 2 and value[5] == 0:
        return 5

    if value[1] == 2 and value[7] ==2 and value[4] == 0:  # ветка 4
        return 4
    elif value[3] == 2 and value[5] == 2 and value[4] == 0:
        return 4

    if value[4] == 2 and value[2] == 2 and value[6] == 0:  # ветка 5
        return 6
    elif value[4] == 2 and value[8] == 2 and value[0] == 0:
        return 0
    elif value[4] == 2 and value[6] == 2 and value[2] == 0:
        return 2
    elif value[4] == 2 and value[0] == 2 and value[8] == 0:
        return 8

    if value[0] == 2 and value[8] == 2 and value[4] == 0:  # ветка 6
        return 4
    elif value[2] == 2 and value[6] == 2 and value[4] == 0:
        return 4
    
    return 9

def logic_defense(value):
    if value[0] == 1 and value[1] == 1 and value[2] == 0:    # ветка 0
        return 2
    elif value[2] == 1 and value[5] == 1 and value[8] == 0:
        return 8
    elif value[8] == 1 and value[7] == 1 and value[6] == 0:
        return 6
    elif value[6] == 1 and value[3] == 1 and value[0] == 0:
        return 0

    if value[1] == 1 and value[2] == 1 and value[0] == 0:  # ветка 1
        return 0
    elif value[5] == 1 and value[8] == 1 and value[2] == 0:
        return 2
    elif value[7] == 1 and value[6] == 1 and value[8] == 0:
        return 8
    elif value[3] == 1 and value[0] == 1 and value[6] == 0:
        return 6

    if value[0] == 1 and value[2] == 1 and value[1] == 0:  # ветка 2
        return 1
    elif value[2] == 1 and value[8] == 1 and value[5] == 0:
        return 5
    elif value[8] == 1 and value[6] == 1 and value[7] == 0:
        return 7
    elif value[6] == 1 and value[0] == 1 and value[3] == 0:
        return 3

    if value[4] == 1 and value[1] == 1 and value[7] == 0:  # ветка 3
        return 7
    elif value[4] == 1 and value[5] == 1 and value[3] == 0:
        return 3
    elif value[4] == 1 and value[7] == 1 and value[1] == 0:
        return 1
    elif value[4] == 1 and value[3] == 1 and value[5] == 0:
        return 5

    if value[1] == 1 and value[7] == 1 and value[4] == 0:  # ветка 4
        return 4
    elif value[3] == 1 and value[5] == 1 and value[4] == 0:
        return 4

    if value[4] == 1 and value[2] == 1 and value[6] == 0:  # ветка 5
        return 6
    elif value[4] == 1 and value[8] == 1 and value[0] == 0:
        return 0
    elif value[4] == 1 and value[6] == 1 and value[2] == 0:
        return 2
    elif value[4] == 1 and value[0] == 1 and value[8] == 0:
        return 8

    if value[0] == 1 and value[8] == 1 and value[4] == 0:  # ветка 6
        return 4
    elif value[2] == 1 and value[6] == 1 and value[4] == 0:
        return 4
    
    return 9

def logic_start_bot(value):
    if not (1 in value):    # 1 ход
        return 4
    elif value.count(1) == 1:   # 3 ход
        if value[0] == 1: # если Х в углу
            return 2
        elif value[2] == 1: # если Х в углу
            return 8
        elif value[8] == 1: # если Х в углу
            return 6
        elif value[6] == 1: # если Х в углу:
            return 0
                                      
        if value[1] == 1:   # если Х по центру боковых сторон
            return 6
        elif value[5] == 1: # если Х по центру боковых сторон
            return 0
        elif value[7] == 1: # если Х по центру боковых сторон
            return 2
        elif value[3] == 1:   # если Х по центру боковых сторон
            return 8

    elif value.count(1) == 2:   # 5 ход
        temp = logic_attack(value)
        if -1 < temp < 9:
            return temp
        temp = logic_defense(value)
        if -1 < temp < 9:
            return temp

        # if (value[0] and value[2]) == 1: # ветка 1
        #     return 6
        # elif (value[1] and value[2]) == 1:
        #     return 0
        # elif (value[5] and value[8]) == 1:
        #     return 2
        # elif (value[7] and value[7]) == 1:
        #     return 8

    elif value.count(1) == 3:
        temp = logic_attack(value)
        if -1 < temp < 9:
            return temp
        temp = logic_defense(value)
        if -1 < temp < 9:
            return temp

        if value[1] == 0 and value[7] == 0:
            return 1
        elif value[3] == 0 and value[5] == 0:
            return 3


        # if (value[0] == 1 and value[6] == 1 and value[7] == 1): # ветка 0
        #     return 5
        # elif (value[3] == 1 and value[0] == 1 and value[2] == 1):
        #     return 7
        # elif (value[1] == 1 and value[2] == 1 and value[8] == 1):
        #     return 3
        # elif (value[6] == 1 and value[8] == 1 and value[5] == 1):
        #     return 1

        # elif (value[0] == 1 and value[5] == 1 and value[6] == 1):   # ветка 1
        #     return 1
        # elif (value[0] == 1 and value[2] == 1 and value[7] == 1):
        #     return 5
        # elif (value[2] == 1 and value[8] == 1 and value[3] == 1):
        #     return 7
        # elif (value[1] == 1 and value[8] == 1 and value[6] == 1):
        #     return 3

        # elif (value[3] == 1 and value[0] == 1 and value[2] == 1):   # ветка 2
        #     return 7
        # elif (value[1] == 1 and value[2] == 1 and value[8] == 1):
        #     return 3
        # elif (value[6] == 1 and value[8] == 1 and value[5] == 1):
        #     return 1
        # elif (value[0] == 1 and value[6] == 1 and value[7] == 1):
        #     return 5

        # elif (value[3] == 1 and value[1] == 1 and value[2] == 1):   # ветка 2 - 2
        #     return 8
        # elif (value[1] == 1 and value[5] == 1 and value[8] == 1):
        #     return 6
        # elif (value[5] == 1 and value[7] == 1 and value[6] == 1):
        #     return 0
        # elif (value[0] == 1 and value[3] == 1 and value[7] == 1):
        #     return 2
    elif value.count(1) == 4:
        for i in range(9):
            if value[i] == 0:
                return i

def logic_start_gamer(value):
    if value.count(1) == 1: # 2 ход
        if value[4] == 1:
            return 0
        return 4
    elif value.count(1) == 2:   # 4 ход
        if value[4] == 1:  
            temp = logic_defense(value)
            if -1 < temp < 9:
                return temp      
            # if value[2] == 1:
            #     return 6
            # elif value[6] == 1:
            #     return 2
            # elif value[1] == 1:
            #     return 7
            # elif value[5] == 1:
            #     return 3
            # elif value[7] == 1:
            #     return 1
            # else:
            #     return 5
            elif value[8] == 1:
                return 2
        else:
            temp = logic_attack(value)
            if -1 < temp < 9:
                return temp
            temp = logic_defense(value)
            if -1 < temp < 9:
                return temp

            if value[0]== 1 and value[8] == 1:    # углы напротив друг друга
                return 1 
            elif value[2]== 1 and value[6] == 1:
                return 5

            elif value[0]== 1 and value[5] == 1:  # середина - дальний угол справа
                return 2
            elif value[2]== 1 and value[7] == 1:
                return 5
            elif value[3]== 1 and value[8] == 1:
                return 7
            elif value[1]== 1 and value[6] == 1:
                return 3

            elif value[0]== 1 and value[7] == 1:    # середина - дальний угол слева
                return 3
            elif value[2]== 1 and value[3] == 1:
                return 1
            elif value[8]== 1 and value[1] == 1:
                return 5
            elif value[6]== 1 and value[5] == 1:
                return 7

            elif value[3]== 1 and value[1] == 1:    # центр - центр рядом
                return 0
            elif value[1]== 1 and value[5] == 1:
                return 2
            elif value[5]== 1 and value[7] == 1:
                return 8
            elif value[7]== 1 and value[3] == 1:
                return 6

            elif value[1]== 1 and value[7] == 1:  # центр - центр напротив
                return 5
            elif value[3]== 1 and value[5] == 1:
                return 1
    elif value.count(1) == 3:   # 6 ход
        if value[4] == 1:
            temp = logic_attack(value)
            if -1 < temp < 9:
                return temp
            temp = logic_defense(value)
            if -1 < temp < 9:
                return temp
        else:
            temp = logic_attack(value)
            if -1 < temp < 9:
                return temp
            temp = logic_defense(value)
            if -1 < temp < 9:
                return temp

            if value[7] == 1 and value[3] == 1 and value[1] == 1: # центр - центр - центр
                return 2
            elif value[3] == 1 and value[1] == 1 and value[5] == 1:
                return 8
            elif value[1] == 1 and value[3] == 1 and value[7] == 1:
                return 6
            elif value[5] == 1 and value[7] == 1 and value[3] == 1:
                return 0

            elif value[3] == 1 and value[1] == 1 and value[8] == 1:   # центр - центп рядом угол напротив
                return 2
            elif value[2] == 1 and value[5] == 1 and value[6] == 1:
                return 8
            elif value[0] == 1 and value[5] == 1 and value[7] == 1:
                return 6
            elif value[2] == 1 and value[7] == 1 and value[3] == 1:
                return 0

            for i in range(9):
                if value[i] == 0:
                    return i
    elif value.count(1) == 4:   # 8 ход
        temp = logic_attack(value)
        if -1 < temp < 9:
            return temp
        temp = logic_defense(value)
        if -1 < temp < 9:
            return temp
        for i in range(9):
            if value[i] == 0:
                return i

print('Если вы хотите начать первым введите 1, ')
print('если хотите чтобы начал бот введите 2, ')
print('если хотите чтобы очередность определил компьютер введите 3')
variant = input('Какой Ваш выбор? Введите число ')

while not is_int(variant) or (int(variant) != 1 and int(variant) != 2 and int(variant) != 3):
    if not is_int(variant):
        variant = input('Это вообше не число, введите 1, 2 или 3 ')
        continue
    elif (int(variant) != 1 and int(variant) != 2 and int(variant) != 3):
        variant = input('Нужно выбрать вариант игры, введите 1, 2 или 3 ')

import random

if variant == '1':
    start_game = False
elif variant == '2':
    start_game = True
else:
    print('Давайте определим кто будет ходить первый и кинем кубик')
    print('Усли выпадет 1, 2, 3 то первым ходите Вы')
    print('Если выпадет 4, 5, 6 то первым ходит бот')
    input('Бросайте кубик, нажмите Enter')
    cube = random.randint(1, 6)
    print(f'Выпало {cube}\n')
    if 0 < cube < 4:
        start_game = False
        print('Ваш ход первый')
    else:
        start_game = True
        print('Первым ходит бот')

f = [f'{i}' for i in range(1, 10)]
b = [0 for i in range(1, 10)]

if start_game:
    for i in range(5):
        t = logic_start_bot(b)
        f[t] = '\033[1m\033[33mO\033[0m'
        b[t] = 2
        print_game()
        if victory(f):
            print('\033[1m\033[33mВам не повезло!!! Я победил!!!\033[0m')
            break
        if i == 4:
            print('\033[1m\033[32mНикто не победил. Ничья\033[0m')
            break

        j = int(input('Введите номер клетки ')) - 1
        f[j] = '\033[1m\033[31mX\033[0m'
        b[j] = 1
        print_game()
        if victory(f):
            print('\033[1m\033[31mПоздравляю, Вы победили!!!\033[0m')
            break
else:
    print_game()
    for i in range(5):
        j = int(input('Введите номер клетки ')) - 1
        f[j] = '\033[1m\033[31mX\033[0m'
        b[j] = 1
        print_game()
        if victory(f):
            print('\033[1m\033[31mПоздравляю, Вы победили!!!\033[0m')
            break
        if i == 4:
            print('\033[1m\033[32mНикто не победил. Ничья\033[0m')
            break
        
        t = logic_start_gamer(b)
        f[t] = '\033[1m\033[33mO\033[0m'
        b[t] = 2
        print_game()
        if victory(f):
            print('\033[1m\033[33mВам не повезло!!! Я победил!!!\033[0m')
            break

print('Game over')    
