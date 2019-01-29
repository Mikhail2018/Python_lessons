#!/usr/bin/python3


"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.
    
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
from random import randint

class Gen_Card:
    def __init__(self, name):
        self.num = [i for i in range(1, 91)]
        self.card = [gen_str_card(self.num), gen_str_card(self.num), gen_str_card(self.num)]
        self.name = name
        self.count_num = 15 

    def __str__(self):
        ui = '{:-^26}\n'.format(self.name)
        for x in range(3):
            ui += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}' \
                       .format(*self.card[x]) + '\n'
        return ui + '--------------------------'

def gen_str_card(num):
        string = ['' for _ in range(9)]
        for x in range(8, 3, -1):
            item = randint(0, x)  
            while string[item] != '': 
                item += 1
            string[item] = num.pop(randint(0, len(num) - 1))
        return string

def main():
    user = Gen_Card(' Ваша карточка ')
    computer = Gen_Card(' Карточка компьютера ')
    num = [i for i in range(1, 91)]
    while True:
        сask = num.pop(randint(0, len(num) - 1))
        print('\nНовый бочонок: {} (осталось {})'.format(сask, len(num)))
        print(user)
        print(computer)
        reply = input('Зачеркнуть цифру? (y/n)')
        reply = reply.lower()
        while len(reply) == 0 or reply not in 'yn':
            print('\n\nНезивестный ввод\n')
            print('Новый бочонок: {} (осталось {})'.format(сask, len(num)))
            print(user)
            print(computer)
            reply = input('Зачеркнуть цифру? (y/n)')
            reply = reply.lower()

        if reply == 'y':
            chk = False
            for x in range(3):
                if сask in user.card[x]:
                    chk = True
                    user.card[x][user.card[x].index(сask)] = '-'
                    user.count_num -= 1
                if сask in computer.card[x]:
                    computer.card[x][computer.card[x].index(сask)] = '-'
                    computer.count_num -= 1
            if chk:
                if user.count_num < 1:
                    print('Вы победили!')
                    break
                elif computer.count_num < 1:
                    print('Компьютер победил!')
                    break
            else:
                print('Вы проиграли! Такого числа в вашей карточке нет')
                break
        elif reply == 'n':
            chk = False
            for x in range(3):
                if сask in user.card[x]:
                    print('Вы проиграли! Такое число есть на вашей карточке!')
                    chk = True
                    break
                if сask in computer.card[x]:
                    computer.card[x][computer.card[x].index(сask)] = '-'
                    computer.count_num -= 1
            if chk:
                break
            if user.count_num < 1:
                print('Вы выиграли!')
                break
            elif computer.count_num < 1:
                print('Компьютер выиграл!')
                break

if __name__ == '__main__':
    main()