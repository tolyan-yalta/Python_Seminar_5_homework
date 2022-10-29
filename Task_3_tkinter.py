# Создайте программу для игры в ""Крестики-нолики"".

def victory(f):
    if f[0] == f[1] == f[2] == 1 or f[0] == f[1] == f[2] == 2:
        return True, f[0]
    elif f[3] == f[4] == f[5] == 1 or f[3] == f[4] == f[5] == 2:
        return True, f[3]
    elif f[6] == f[7] == f[8] == 1 or f[6] == f[7] == f[8] == 2:
        return True, f[6]
    elif f[0] == f[3] == f[6] == 1 or f[0] == f[3] == f[6] == 2:
        return True, f[0]
    elif f[1] == f[4] == f[7] == 1 or f[1] == f[4] == f[7] == 2:
        return True, f[1]
    elif f[2] == f[5] == f[8] == 1 or f[2] == f[5] == f[8] == 2:
        return True, f[2]
    elif f[0] == f[4] == f[8] == 1 or f[0] == f[4] == f[8] == 2:
        return True, f[0]
    elif f[2] == f[4] == f[6] == 1 or f[2] == f[4] == f[6] == 2:
        return True, f[2]
    else:
        return False, None

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
    elif value.count(1) == 5:
        if value[4] == 1:
            return 0
        return 4


def clear_field():
    global b
    global count
    b = [0 for i in range(1, 10)]
    btn_gamer.config(command=start_gamer, relief='raised')
    btn_bot.config(command=start_bot, relief='raised')
    btn1.config(command=press_btn1, image='', relief='raised')
    btn2.config(command=press_btn2, image='', relief='raised')
    btn3.config(command=press_btn3, image='', relief='raised')
    btn4.config(command=press_btn4, image='', relief='raised')
    btn5.config(command=press_btn5, image='', relief='raised')
    btn6.config(command=press_btn6, image='', relief='raised')
    btn7.config(command=press_btn7, image='', relief='raised')
    btn8.config(command=press_btn8, image='', relief='raised')
    btn9.config(command=press_btn9, image='', relief='raised')
    label_finish1.config(text='')
    label_finish2.config(image='')
    count = 0

def start_bot():
    global bot
    global b
    global count
    bot = True
    btn_gamer.config(command=0, relief='sunken')
    b[logic_start_bot(b)] = 2
    btn5.config(command=0, image=blue_zero, relief='sunken')
    count += 1

def start_gamer():
    global bot
    bot = False
    btn_bot.config(command=0, relief='sunken')

def finish(champion):
    label_finish1.config(text='Победил:')
    if champion == 2:
        label_finish2.config(image=blue_zero)
    else:
        label_finish2.config(image=red_cross)

def press_button_1_9(index):
    global bot
    global b
    if bot:
        btn_1_9[index].config(command=0 , image=red_cross, relief='sunken')
        b[index] = 1
        temp = logic_start_bot(b)
        btn_1_9[temp].config(command=0, image=blue_zero, relief='sunken')
        b[temp] = 2
    else:
        btn_1_9[index].config(command=0 , image=red_cross, relief='sunken')
        b[index] = 1
        temp = logic_start_gamer(b)
        btn_1_9[temp].config(command=0, image=blue_zero, relief='sunken')
        b[temp] = 2
    global count
    count += 1
    vict, champion = victory(b)
    if vict:
        finish(champion)
    if count == 5:
        label_finish1.config(text='         Ничья!')

b = [0 for i in range(1, 10)]

bot = None
count = 0

def press_btn1():
    index = 0
    press_button_1_9(index)
def press_btn2():
    index = 1
    press_button_1_9(index)
def press_btn3():
    index = 2
    press_button_1_9(index)
def press_btn4():
    index = 3
    press_button_1_9(index)
def press_btn5():
    index = 4
    press_button_1_9(index)
def press_btn6():
    index = 5
    press_button_1_9(index)
def press_btn7():
    index = 6
    press_button_1_9(index)
def press_btn8():
    index = 7
    press_button_1_9(index)
def press_btn9():
    index = 8
    press_button_1_9(index)

import tkinter as tk

win = tk.Tk()
win.title('Крестики-нолики')

w = 480 	# width - ширина
h = 720    # height - высота
sw = win.winfo_screenwidth()    # определяем ширину экрана
x = int((sw - w) / 2)
sh = win.winfo_screenheight()   # определяем высоту экрана
y = int((sh - h) / 2)

win.geometry(f"{w}x{h}+{x}+{y}")
win.resizable(False, False)

photo = tk.PhotoImage(file='game-controller.png')
win.iconphoto(False, photo)

red_cross = tk.PhotoImage(file='red_cross130.png')
blue_zero = tk.PhotoImage(file='blue_zero130.png')

btn_gamer = tk.Button(win, text='Начинает игрок', command=start_gamer, font=('times new roman',14, 'bold'))
raised_01 = tk.Button(win, text='', bg='blue', relief=tk.RAISED, state=tk.DISABLED)
btn_clear = tk.Button(win, text='Очистить поле', command=clear_field , font=('times new roman',14, 'bold'))
raised_02 = tk.Button(win, text='', bg='blue', relief=tk.RAISED, state=tk.DISABLED)
btn_bot = tk.Button(win, text='Начинает бот', command=start_bot, font=('times new roman',14, 'bold'))

btn1 = tk.Button(win, text='', command=press_btn1)
raised_1 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn2 = tk.Button(win, text='', command=press_btn2)
raised_2 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn3 = tk.Button(win, text='', command=press_btn3)
raised_3 = tk.Label (win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED, height=1, font=('Arial',5))

btn4 = tk.Button(win, text='', command=press_btn4)
raised_4 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn5 = tk.Button(win, text='', command=press_btn5)
raised_5 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn6 = tk.Button(win, text='', command=press_btn6)
raised_6 = tk.Label (win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED, height=1, font=('Arial',5))

btn7 = tk.Button(win, text='', command=press_btn7)
raised_7 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn8 = tk.Button(win, text='', command=press_btn8)
raised_8 = tk.Button(win, text='', bg='green', relief=tk.RAISED, state=tk.DISABLED)
btn9 = tk.Button(win, text='', command=press_btn9)

label_finish1 = tk.Label(win, text='', font=('times new roman',44, 'bold'))
label_finish2 = tk.Label(win, text='')

btn_gamer.grid(row=0, column=0, sticky='wens')
raised_01.grid(row=0, column=1, sticky='ns')
btn_clear.grid(row=0, column=2, sticky='wens')
raised_02.grid(row=0, column=3, sticky='ns')
btn_bot.grid(row=0, column=4, sticky='wens')

btn1.grid(row=1, column=0, sticky='wens')
raised_1.grid(row=1, column=1, sticky='ns')
btn2.grid(row=1, column=2, sticky='wens')
raised_2.grid(row=1, column=3, sticky='ns')
btn3.grid(row=1, column=4, sticky='wens')
raised_3.grid(row=2, column=0, columnspan=5, sticky='we')

btn4.grid(row=3, column=0, sticky='wens')
raised_4.grid(row=3, column=1, sticky='ns')
btn5.grid(row=3, column=2, sticky='wens')
raised_5.grid(row=3, column=3, sticky='ns')
btn6.grid(row=3, column=4, sticky='wens')
raised_6.grid(row=4, column=0, columnspan=5, sticky='we')

btn7.grid(row=5, column=0, sticky='wens')
raised_7.grid(row=5, column=1, sticky='ns')
btn8.grid(row=5, column=2, sticky='wens')
raised_8.grid(row=5, column=3, sticky='ns')
btn9.grid(row=5, column=4, sticky='wens')

label_finish1.grid(row=6, column=0, columnspan=4)
label_finish2.grid(row=6, column=4, sticky='wens')

btn_1_9 = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

win.grid_rowconfigure(0, minsize=50)
win.grid_rowconfigure(1, minsize=150)
win.grid_rowconfigure(2, minsize=5)
win.grid_rowconfigure(3, minsize=150)
win.grid_rowconfigure(4, minsize=5)
win.grid_rowconfigure(5, minsize=150)
win.grid_rowconfigure(6, minsize=150)
win.grid_rowconfigure(7, minsize=50)
win.grid_columnconfigure(0, minsize=150)
win.grid_columnconfigure(1, minsize=5)
win.grid_columnconfigure(2, minsize=150)
win.grid_columnconfigure(3, minsize=5)
win.grid_columnconfigure(4, minsize=150)

tk.Button(win, text='Закрыть игру', command=win.quit, font=('times new roman',14, 'bold')).grid(row=7, column=0, columnspan=5, sticky='we')

win.mainloop()