# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

from random import randint


def input_dat(name):
    x = int(input(f"{name}, Введите количество конфет, которое возьмете: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, Введите количество конфет от 1 до 28: "))
    return x


def p_print(name, k, counter, value):
    print(
        f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
turn = randint(0, 2)
if turn:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if turn:
        k = input_dat(player1)
        counter1 += k
        value -= k
        turn = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        turn = True
        p_print(player2, k, counter2, value)

if turn:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
