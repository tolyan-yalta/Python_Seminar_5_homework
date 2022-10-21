# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('Task_1.txt', 'r', encoding='utf-8') as f:
    text = f.readline()

text = ' '.join(filter(lambda x: 'абв' not in x, text.split()))
print(text)

with open('Task_1.txt', 'a', encoding='utf-8') as f:
    f.write(text + '\n')
    