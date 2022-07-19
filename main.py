# Учим детей таблице умножения

import importlib
import multi

answer = 0
print('****Привет! Немного поумножаем!')

while answer != '-':
    answer = input()
    if answer == '-':
        break
    elif answer == '+':
        print('Отлично! Играем дальше!')
        importlib.reload(multi)

print('Пока! Я буду скучать без тебя!!!')
input()
