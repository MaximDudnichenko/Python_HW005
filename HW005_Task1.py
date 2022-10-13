# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

def bets(opt, players, max_bet, value_candys):
    if opt == 1:
        take_candy = int(input(f'{players[2]}, введите количество конфет, которое вы возьмете (от 1 до {max_bet}): '))
    elif opt == 2:
        take_candy = random.randint(1, max_bet)
        print(f'{players[2]} берет {take_candy} конфет(ы)')
    else:
        if value_candys % 29 != 0:
            take_candy = value_candys % 29
        else:
            take_candy = random.randint(1, 5)
        print(f'{players[2]} берет {take_candy} конфет(ы)')
    return take_candy

print('Выберите вариант игры:\n 1 - с человеком\n 2 - с ботом\n 3 - с "умным" ботом')
option = int(input())
if option < 1 or option > 3:
    print('Такого варианта игры нет')
else:
    players = {}
    players[1] = input('Введите имя игрока 1: ')
    if option == 1:
        players[2] = input('Введите имя игрока 2: ')
    else:
        players[2] = 'bot'
    print(f'Второй игрок {players[2]}')

    j = random.randint(1,2)
    print('Первым ходит ', players[j])

    candys = 2021
    print(f'Конфет на столе - {candys}')
    status = True
    while status:
        if candys >= 28:
            max_bet = 28
        else:
            max_bet = candys
        
        if j == 1:
            bet = int(input(f'{players[1]}, введите количество конфет, которое вы возьмете (от 1 до {max_bet}): '))
        else:
            bet = bets(option, players, max_bet, candys)
        if bet > 0 and bet <= max_bet:
            candys -= bet
            if candys > 0:
                print(f'Конфет на столе - {candys}')
                if j == 1:
                    j = 2
                else:
                    j = 1
            else:
                print(f'На столе не осталось конфет')
                status = False
        else:
            print(f'Введите правильное количество конфет (от 1 до {max_bet}')

    print(f'Поздравляю! Выиграл {players[j]}')