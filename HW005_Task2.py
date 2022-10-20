# Создайте программу для игры в "Крестики-нолики".

from dataclasses import field

def print_field(field):
    for item in field:
        print(item)

def user_motion():
    while True:
        motion = input('Введите через пробел номер строки и номер столбеца (1-3), в который хотите поставить свой знак: ')
        cell = [int(i) for i in motion.split()]
        if cell[0] > 0 and cell[0] < 4 and cell[1] > 0 and cell[1] < 4:
            cell[0] = cell[0] - 1
            cell[1] = cell[1] - 1
            break
    return cell

def occupy_field(field, sing, cell):
    a = True
    while a == True:
        if field[cell[0]][cell[1]] == ' ':
            field[cell[0]][cell[1]] = sing
            a = False
        else:
            print('Невозможно сделать ход')
            cell = user_motion()
    print_field(field)
    return field

def win_control(win, field, cell, sing):
    if field[cell[0]][0] == sing and field[cell[0]][1] == sing and field[cell[0]][2] == sing:
        win = True
    elif field[0][cell[1]] == sing and field[1][cell[1]] == sing and field[2][cell[1]] == sing:
        win = True
    elif field[0][0] == sing and field[1][1] == sing and field[2][2] == sing:
        win = True
    elif field[0][2] == sing and field[1][1] == sing and field[2][0] == sing:
        win = True
    return win

def field_control(field):
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if field[i][j] != ' ':
                count += 1
    return count


field_of_play = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print_field(field_of_play)
sing = 'O'
win = False
while win == False:
    if sing == 'X':
        sing = 'O'
    else:
        sing = 'X' 
    cell = user_motion()
    field_of_play = occupy_field(field_of_play, sing, cell)
    win = win_control(win, field_of_play, cell, sing)
    count = field_control(field_of_play)
    if count == 9 and win == False:
        print('Ничья')
        break
    elif win == True:
        print(f'Победа {sing}')

