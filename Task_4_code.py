# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Модуль сжатия

# Программа берет изображение из файла Task_4_panda.txt, сжимает 
# и записывает в файл Task_4_code.txt

# Обратный процесс выполняется в файле Task_4_decode.py

number = {0: '¶', 1: '☺', 2: '☻', 3: '♥', 4: '♦', 5: '♣', 6: '►', 7: '◄', 8: '↕', 9: '‼'}

with open('Task_4_panda.txt', 'r', encoding='utf-8') as f:
    raw = f.read()

for i in range(10):
    if str(i) in raw:
        raw = raw.replace(str(i), number.get(i))

new_raw = ''
count_simbol = 1
for i in range(len(raw)-1):
    if ord((raw[i])) == ord((raw[i+1])):
        count_simbol += 1
        if i == len(raw)-2:
            new_raw = new_raw + str(count_simbol) + raw[i]
        continue
    elif count_simbol == 1:
        if i == len(raw)-2:
            new_raw = new_raw + raw[i] + raw[i+1]
        new_raw = new_raw + raw[i]
    elif count_simbol > 1:
        if i == len(raw)-2:
            new_raw = new_raw + str(count_simbol) + raw[i] + raw[i+1]
        else:
            new_raw = new_raw + str(count_simbol) + raw[i]
        count_simbol = 1

with open('Task_4_code.txt', 'ab') as f:
    f.write(new_raw.encode('utf-8'))

