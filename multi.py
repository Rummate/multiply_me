import random as rnd
import time
from statistics import median

print('Вот первый пример:')
tasknum = rnd.randint(8, 12)  # кол-во задач, которые решаем - от 10 до 15

decis_stk = []  # список пользовательских вариантов ответов
trueprod_stk = []  # список правильных ответов
mult_stk = []  # список _пар_ сомножителей
time_stk = []
corrects = 0  # кол-во верных ответов
mistakes = 0  # кол-во ошибочных ответов
attempts = 0  # кол-во попыток ответа на данный пример

for iterations in range(tasknum):  # решаем tasknum примеров

    mult1 = rnd.randint(3, 9)
    mult2 = rnd.randint(3, 9)

    mults = [mult1, mult2]  # запоминаем сомножители в список
    mult_stk.append(mults)  # каждый пример записываем в список

    trueprod = mult1 * mult2  # вычисляем правильное произведение
    trueprod_stk.append(trueprod)  # записываем правильное произведение в отд. в список

    print(mult1, 'X', mult2, '=')
    t1 = time.time()

    decision = 0
    temp_decis = []  # список вводимых вариантов решений данного примера. Обнуляется каждый цикл

    while trueprod != decision:  # по умолчанию  decision = 0 => заходим в цикл, не выходим, пока не решим верно.
        decision = input()  # просим ввести вариант ответа

        while True:  # проверка правильности ввода
            try:
                decision = int(decision)  # проверку проходим, если ввод преобразуется в целое, иначе повторный ввод
                break
            except ValueError:
                print('Ответ должен состоять из цифр, введите ещё раз:')
                decision = input()

        attempts = attempts + 1  # увеличиваем счетчик попыток после проверки корректности ввода
        temp_decis.append(decision)  # записываем  вар-т ответа во вложенный список вариантов ответов

        if decision > trueprod:  # ответ в правильном формате, но неверный => подсказываем, он больше верного или меньше
            print('ПЕРЕЛЁТ!. Ответ меньше на ', decision - trueprod, '\n Пробуем еще раз:')
            mistakes = mistakes + 1
        elif decision < trueprod:
            print('НЕДОЛЁТ!. Ответ больше на ', trueprod-decision,  '\nПробуем еще раз:')
            mistakes = mistakes + 1

    t2 = time.time()
    decis_stk.append(temp_decis)  # записываем вложенным в общий списком все введенные варианты ответов на данный пример
    corrects = corrects + 1  # увеличиваем счетчик правильных ответов
    print('Верно!!!')
    time_stk.append(t2-t1)

    if iterations < tasknum - 1:  # пишет "след. пример" для всех итераций, кроме первой и последней
        print('Следующий пример:')


print('***ПОСМОТРИМ РЕЗУЛЬТАТ***\n')
print('Ты сделал ', mistakes, ' ошибок в ', attempts, 'попытках. \nПроцент ошибок: ',
      round(mistakes / attempts * 100, 0),
      '\nСреднее время на пример:', round(median(time_stk), 1), 'секунд',
      '\nСамое большое время на пример:', round(max(time_stk), 1), 'секунд',
      '\nНажми любую клавишу...'); input()

# После результатов вывести все ошибочные примеры
if mistakes == 0:
    print("РЕШЕНО БЕЗ ОШИБОК!!!")
else:  # выполняем работу над ошибками:

    rno_list = []  # - сюда запишем пары множителей ошибок из списка mult_stk
    for u in range(len(decis_stk)):
        if len(decis_stk[u]) != 1:  # если ответ дан с 1-го раза, длина элементов списка decis_stk[u] будет = 1. Если больше => была ошибка
            rno_list.append(mult_stk[u])

    print('Вот примеры, в которых ты ошибся.')
    for k in range(len(rno_list)):
        print(rno_list[k][0], ' x ', rno_list[k][1], ' = ', rno_list[k][0] * rno_list[k][1])
    print('Выучи их и нажми любую клавишу, чтобы продолжить...'); input()

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Р А Б О Т А  Н А Д  О Ш И Б К А М И \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Введи ответ:')
    rnd.shuffle(rno_list)  # перемешиваем примеры Р.Н.О., чтобы были в произвольном порядке
    for v in range(len(rno_list)):
        mult1 = rno_list[v][0]
        mult2 = rno_list[v][1]
        trueprod = mult1 * mult2
        print(mult1, 'X', mult2, '=')
#
        # решаем пример из РНО так же, как в "теле" тренажера, но без записи в результатов в списки
        decision = 0
#
        while trueprod != decision:
            decision = input()  # просим ввести вариант ответа
            while True:  # проверка правильности ввода
                try:
                    decision = int(decision)
                    break
                except ValueError:
                    print('Ответ должен состоять из цифр, введите ещё раз:')
                    decision = input()
            if decision > trueprod:  # подсказываем ответ - больше верного или меньше
                print('Перелёт!. Пробуем еще раз:')
            elif decision < trueprod:
                print('Недолёт!. Пробуем еще раз:')

    print('Верно!!!')

    if v < len(rno_list) - 1:  # пишет "след. пример" для всех итераций, кроме первой и последней
        print('Следующий пример:')

print('МОЛОДЕЦ! ОТЛИЧНАЯ РАБОТА!\n Введи [+] для того чтобы сыграть еще раз \n или [-], чтобы выйти')
