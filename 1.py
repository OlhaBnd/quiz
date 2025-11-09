from turtle import*
from random import randint

size = 100
def start(x, y):
    penup()
    goto(x, y)
    pendown()

def field(col):
    xStart, yStart = -100, 100
    x, y = xStart, yStart
    color(col)
    width(10)
    for i in range(3):
        for j in range(3):
            start(x, y)
            for d in range(4):
                fd(size)
                rt(90)
            x += size
        x = xStart
        y -= size

def draw_cross(x, y, col):
    cx = x + size // 2
    cy = y - size // 2
    color(col)
    width(10)
    #перша діагональ
    penup()
    goto(cx - 0.5*size, cy - 0.5*size)
    pendown()
    goto(cx + 0.5*size, cy + 0.5*size)
    
    #друга діагональ
    penup()
    goto(cx - 0.5*size, cy + 0.5*size)
    pendown()
    goto(cx + 0.5*size, cy - 0.5*size)
    penup()
    setheading(0)

def draw_dot(x, y, col):
    cx = x + size // 2
    cy = y - size // 2
    penup()
    goto(cx, cy-size //2)
    pendown()
    color(col)
    width(5)
    circle(size//2)
    penup()
    setheading(0)

def move_player(player, col):
    cell = int(input("Введіть номер клітинки (1-9): "))
    while playing_field[cell] != -1:
        print("Клітинка вже занята, оберіть іншу!")
        cell = int(input("Введіть номер клітинки (1-9): "))
    x, y, = x_cor[cell], y_cor[cell]
    playing_field[cell] = player
    if player == 1:
        draw_cross(x, y, col)
    else:
        draw_dot(x, y, col)
    return -1

def check_win():
    """Перевіряє, чи є переможець"""
    combos = [
        (1, 2, 3, 1, 0), (4, 5, 6, 5, 0), (7, 8, 9, 7, 0),  # горизонтальні комбінації
        (1, 4, 7, 1, 270), (2, 5, 8, 2, 270), (3, 6, 9, 3, 270),  # вертикальні
        (1, 5, 9, 1, 315), (3, 5, 7, 3, 225)  # діагональні
    ]
    for a, b, c, cell, h in combos:
        if playing_field[a] == playing_field[b] == playing_field[c] and playing_field[a] != -1:
            return playing_field[a], cell, h  # Повертаємо гравця, клітинку та кут для перемоги
    return -1, 0, 0  # Ніхто не виграв




