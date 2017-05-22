from random import *

print("***         Игра Кости           ***")
print('''
    *************  *************
    *           *  *           *
    *  O     0  *  *           *
    *           *  *           *
    *     O     *  *     O     *
    *           *  *           *
    *  O     O  *  *           *
    *           *  *           *
    *************  *************
''')

print("*    Введите Имя первого игрока    *")
p1_name = str(input())
print("*    Введите имя второго игрока    *")
p2_name = str(input())

sp_one = 0
sp_tho = 0


def sumplayer(x):
    if x == 1:
        global sp_one
        sp_one += 1
    elif x == 2:
        global sp_tho
        sp_tho += 1
    else:
        pass


def score():
    print("Счет " + str(sp_one) + ":" + str(sp_tho) + "\n")


def player():
    print("Бросает кость  " + p1_name)
    input()
    p1_val = randint(1, 6)
    print("Выпала кость  = " + str(p1_val) + "\n")
    print("Бросает кость " + p2_name)
    input()
    p2_val = randint(1, 6)
    print("Выпала кость  = " + str(p2_val) + "\n")
    if p1_val > p2_val:
        sumplayer(1)
        print("Игрок " + p1_name + " Выиграл\n")
        score()
    elif p1_val == p2_val:
        print("Ничья\n")
        score()

    elif p1_val < p2_val:
        sumplayer(2)
        print("Игрок " + p2_name + " Выиграл\n")
        score()
    else:
        pass


while True:
    print("="*36,"\n")
    player()
