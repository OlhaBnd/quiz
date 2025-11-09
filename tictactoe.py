from turtle import*
from random import randint

speed(0)
size = 100
playing_field = [None, -1, -1, -1, -1, -1, -1, -1, -1, -1] 
x_cor = [None, -100, 0, 100, -100, 0, 100, -100, 0, 100]
y_cor = [None, 100, 100, 100, 0, 0, 0, -100, -100, -100]
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
def crossOut(cell, h, who):
    """Малює лінію перемоги через центр клітинок"""
    x, y = x_cor[cell], y_cor[cell]
    cx = x + size // 2  # Центр клітинки по X
    cy = y - size // 2  # Центр клітинки по Y

    color("green")
    width(7)
    
    if h == 0:  # Горизонтальна лінія
        penup()
        goto(cx - 1.5*size, cy)
        pendown()
        goto(cx + 1.5*size, cy)
    elif h == 270:  # Вертикальна лінія
        penup()
        goto(cx, cy + 1.5*size)
        pendown()
        goto(cx, cy - 1.5*size)
    else:  # Діагоналі
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
    return -1 not in playing_field  # Якщо -1 немає, всі клітинки зайняті
field("black")               # Малюємо ігрове поле чорного кольору
player = randint(0, 1)       # Випадково обираємо, хто ходить перший (0 або 1)

while True:
    if player == 1:
        move_player(player, "red")   # Хід хрестика
        player = 0
    else:
        move_player(player, "blue")  # Хід нулика
        player = 1

    win, cell, h = check_win()  # Перевіряємо переможця
    if win == 1:
        crossOut(cell, h, "Хрестик")  # Малюємо лінію перемоги
        break
    elif win == 0:
        crossOut(cell, h, "Нулик")    # Малюємо лінію перемоги
        break

    if check_no_one_won():            # Якщо всі клітинки зайняті
        write("Нічия!", font=("Arial", 20, "bold"))
        break

done()  # Завершуємо роботу черепахи і зберігаємо вікно


