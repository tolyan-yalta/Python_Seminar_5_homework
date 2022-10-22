# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Модуль восстановления

# Программа берет сжатые данные из файла Task_4_code.txt и
# распаковывает их в файл Task_4_decode.txt

number_decode = {'¶': 0, '☺': 1, '☻': 2, '♥': 3, '♦': 4, '♣': 5, '►': 6, '◄': 7, '↕': 8, '‼': 9}

with open('Task_4_code.txt', 'rb') as f:
    raw = f.read().decode(encoding='utf-8')

new_raw = ''
t = ''
i = 0
while i < (len(raw)):
    if chr(48) <= raw[i] <= chr(57):
        t = t + raw[i]
        if chr(48) <= raw[i+1] <= chr(57):
            i += 1
            continue
        else:
            new_raw = new_raw + raw[i+1] * int(t)
            i += 2
            t = ''
            continue
    elif raw[i] < chr(48) or raw[i] > chr(57):
        new_raw = new_raw + raw[i]
        i += 1
        continue  
    
key_decode = number_decode.keys()

for i in key_decode:

    if i in new_raw:
        new_raw = new_raw.replace(i, str(number_decode.get(i)))
print(new_raw) 
    
with open('Task_4_decode.txt', 'a', encoding='utf-8') as f:
    f.write(new_raw)

