from turtle import *
from random import randint

# === Налаштування ===
speed(0)
size = 100
playing_field = [None, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# координати центрів клітинок
x_cor = [None, -100, 0, 100, -100, 0, 100, -100, 0, 100]
y_cor = [None, 100, 100, 100, 0, 0, 0, -100, -100, -100]

# === Допоміжні функції ===
def start(x, y):
    """Переміщає курсор без малювання у вказану позицію"""
    penup()
    goto(x, y)
    pendown()

def field(col):
    """Малює ігрове поле"""
    xStart, yStart = -100, 100

    x, y = xStart, yStart
    color(col)
    width(10)
    for i in range(3):
        for j in range(3):
            start(x, y)
            for _ in range(4):
                forward(size)
                right(90)
            x += size
        x = xStart
        y -= size

def draw_cross(x, y, col):
    """Малює хрестик, центрований у клітинці"""
    cx = x + size // 2
    cy = y - size // 2
    color(col)
    width(10)

    # Перша діагональ
    penup()
    goto(cx - 0.5*size, cy - 0.5*size)
    pendown()
    goto(cx + 0.5*size, cy + 0.5*size)

    # Друга діагональ
    penup()
    goto(cx - 0.5*size, cy + 0.5*size)
    pendown()
    goto(cx + 0.5*size, cy - 0.5*size)
    penup()
    setheading(0)

def draw_dot(x, y, col):
    """Малює нулик, центрований у клітинці"""
    cx = x + size // 2
    cy = y - size // 2
    penup()
    goto(cx, cy - size // 2)  # circle малює від краю
    pendown()
    color(col)
    width(5)
    circle(size // 2)
    penup()
    setheading(0)

def move_player(player, col):
    """Обробляє хід гравця"""
    cell = int(input("Введіть номер клітинки (1-9): "))
    while playing_field[cell] != -1:
        print("Клітинка вже зайнята! Оберіть іншу.")
        cell = int(input("Введіть номер клітинки (1-9): "))

    x, y = x_cor[cell], y_cor[cell]
    playing_field[cell] = player
    if player == 1:
        draw_cross(x, y, col)
    else:
        draw_dot(x, y, col)
    return -1

def check_win():
    """Перевіряє, чи є переможець"""
    combos = [
        (1, 2, 3, 1, 0), (4, 5, 6, 5, 0), (7, 8, 9, 7, 0),  # горизонталі
        (1, 4, 7, 1, 270), (2, 5, 8, 2, 270), (3, 6, 9, 3, 270),  # вертикалі
        (1, 5, 9, 1, 315), (3, 5, 7, 3, 225)  # діагоналі
    ]
    for a, b, c, cell, h in combos:
        if playing_field[a] == playing_field[b] == playing_field[c] and playing_field[a] != -1:
            return playing_field[a], cell, h
    return -1, 0, 0

def crossOut(cell, h, who):
    """Малює лінію перемоги"""
    x, y = x_cor[cell], y_cor[cell]
    cx = x + size // 2  # центр клітинки
    cy = y - size // 2

    color("green")
    width(7)
    
    if h == 0:  # горизонтальна
        penup()
        goto(cx - 1.5*size, cy)
        pendown()
        goto(cx + 1.5*size, cy)
    elif h == 270:  # вертикальна
        penup()
        goto(cx, cy + 1.5*size)
        pendown()
        goto(cx, cy - 1.5*size)
    else:  # діагоналі
        penup()
        goto(cx - 1.5*size, cy - 1.5*size)
        pendown()
        goto(cx + 1.5*size, cy + 1.5*size)

    penup()
    goto(0, 0)
    write(f"Виграв: {who}", align="center", font=("Arial", 20, "bold"))
    setheading(0)


def check_no_one_won():
    """Перевіряє, чи залишились вільні клітинки"""
    return -1 not in playing_field

# === Основна логіка гри ===
field("black")
player = randint(0, 1)

while True:
    if player == 1:
        move_player(player, "red")
        player = 0
    else:
        move_player(player, "blue")
        player = 1

    win, cell, h = check_win()
    if win == 1:
        crossOut(cell, h, "Хрестик")
        break
    elif win == 0:
        crossOut(cell, h, "Нулик")
        break

    if check_no_one_won():
        write("Нічия!", font=("Arial", 20, "bold"))
        break

done()
