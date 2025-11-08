from turtle import *      # Імпортуємо все з модуля turtle для малювання графіки
from random import randint # Імпортуємо функцію randint для випадкового вибору гравця

# === Налаштування ===
speed(0)                  # Встановлюємо максимально швидку анімацію черепахи
size = 100                # Розмір клітинки поля
playing_field = [None, -1, -1, -1, -1, -1, -1, -1, -1, -1]  
# Масив для збереження стану клітинок: -1 = вільна, 0 = нулик, 1 = хрестик
# Індекс 0 не використовується для зручності нумерації клітинок від 1 до 9

# координати верхнього лівого кута клітинок (для малювання)
x_cor = [None, -100, 0, 100, -100, 0, 100, -100, 0, 100]
y_cor = [None, 100, 100, 100, 0, 0, 0, -100, -100, -100]

# === Допоміжні функції ===
def start(x, y):
    """Переміщає курсор без малювання у вказану позицію"""
    penup()   # Піднімаємо перо, щоб не малювати
    goto(x, y) # Переміщаємо черепаху в координати (x, y)
    pendown()  # Опускаємо перо, щоб почати малювати

def field(col):
    """Малює ігрове поле 3x3"""
    xStart, yStart = -100, 100  # Верхній лівий кут сітки

    x, y = xStart, yStart
    color(col)    # Встановлюємо колір ліній
    width(10)     # Встановлюємо товщину ліній
    for i in range(3):      # Рядки
        for j in range(3):  # Стовпчики
            start(x, y)     # Переміщаємося у верхній лівий кут клітинки
            for _ in range(4):  # Малюємо квадрат
                forward(size)
                right(90)
            x += size      # Переходимо до наступної клітинки по горизонталі
        x = xStart          # Повертаємося до початку рядка
        y -= size           # Переходимо до наступного рядка

def draw_cross(x, y, col):
    """Малює хрестик у центрі клітинки"""
    cx = x + size // 2  # Обчислюємо центр клітинки по X
    cy = y - size // 2  # Обчислюємо центр клітинки по Y
    color(col)          # Встановлюємо колір
    width(10)           # Товщина ліній

    # Перша діагональ
    penup()
    goto(cx - 0.5*size, cy - 0.5*size) # Початок діагоналі
    pendown()
    goto(cx + 0.5*size, cy + 0.5*size) # Кінець діагоналі

    # Друга діагональ
    penup()
    goto(cx - 0.5*size, cy + 0.5*size)
    pendown()
    goto(cx + 0.5*size, cy - 0.5*size)
    penup()
    setheading(0)  # Повертаємо напрямок черепахи на 0 градусів

def draw_dot(x, y, col):
    """Малює нулик у центрі клітинки"""
    cx = x + size // 2  # Центр клітинки по X
    cy = y - size // 2  # Центр клітинки по Y
    penup()
    goto(cx, cy - size // 2)  # Позиціюємо черепаху так, щоб circle малював від краю
    pendown()
    color(col)
    width(5)
    circle(size // 2)   # Малюємо коло (нулик)
    penup()
    setheading(0)

def move_player(player, col):
    """Обробляє хід гравця"""
    cell = int(input("Введіть номер клітинки (1-9): "))  # Вводимо номер клітинки
    while playing_field[cell] != -1:  # Перевірка, чи клітинка вільна
        print("Клітинка вже зайнята! Оберіть іншу.")
        cell = int(input("Введіть номер клітинки (1-9): "))

    x, y = x_cor[cell], y_cor[cell]   # Отримуємо координати клітинки
    playing_field[cell] = player      # Записуємо хід гравця в масив
    if player == 1:
        draw_cross(x, y, col)  # Малюємо хрестик
    else:
        draw_dot(x, y, col)    # Малюємо нулик
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

# === Основна логіка гри ===
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
