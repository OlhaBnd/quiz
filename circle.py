# Імпортуємо бібліотеку pygame та randint для випадкових чисел
import pygame
from random import randint

# Ініціалізуємо pygame
pygame.init()

# Створюємо вікно гри
WIDTH, HEIGHT = 800, 600                       # ширина та висота екрана
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мінімальна гра з Circle")
clock = pygame.time.Clock()                    # об'єкт для контролю FPS

# Створюємо платформу (прямокутник)
platform = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 40, 120, 20)  # позиція і розмір
platform_speed = 10                                             # швидкість руху платформи


# Клас Circle — описує м'яч
class Circle:
    def __init__(self, x, y, radius, speed, color):
        # Початкові координати кола
        self.x = x
        self.y = y
        # Радіус кола
        self.radius = radius
        # Швидкість по осях X і Y
        self.dx = speed
        self.dy = -speed
        # Колір кола
        self.color = color

    # Метод руху м'яча
    def move(self):
        self.x += self.dx    # змінюємо координату X
        self.y += self.dy    # змінюємо координату Y

        # Якщо м'яч доторкається лівої або правої межі — змінюємо напрям
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.dx *= -1

        # Якщо м'яч доторкається верхньої межі — змінюємо напрям
        if self.y - self.radius <= 0:
            self.dy *= -1

    # Метод малювання кола на екрані
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    # Перевірка зіткнення м'яча з платформою
    def collide_with(self, rect):
        # Якщо нижня точка м'яча торкається платформи
        if rect.collidepoint(self.x, self.y + self.radius):
            self.dy *= -1   # міняємо напрям руху по вертикалі


# Створюємо м'яч
ball = Circle(WIDTH // 2, HEIGHT // 2, 15, 6, (255, 255, 255))

# Головний цикл гри
running = True
while running:
    # Обробка подій
    for e in pygame.event.get():
        if e.type == pygame.QUIT:     # якщо натиснуто "х" — вихід
            running = False

    # Отримуємо натиснуті клавіші
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:              # рух вліво (клавіша A)
        platform.x -= platform_speed
    if keys[pygame.K_d]:              # рух вправо (клавіша D)
        platform.x += platform_speed

    # Обмеження руху платформи в межах екрана
    if platform.left < 0:
        platform.left = 0
    if platform.right > WIDTH:
        platform.right = WIDTH

    # Рух м'яча
    ball.move()
    # Перевірка зіткнення з платформою
    ball.collide_with(platform)

    # Якщо м'яч падає нижче екрана — створюємо новий у центрі
    if ball.y - ball.radius > HEIGHT:
        ball = Circle(WIDTH // 2, HEIGHT // 2, 15, 6, (255, 255, 255))

    # Малюємо фон
    window.fill((0, 0, 0))
    # Малюємо м'яч
    ball.draw(window)
    # Малюємо платформу
    pygame.draw.rect(window, (0, 255, 255), platform, border_radius=10)

    # Оновлюємо зображення на екрані
    pygame.display.flip()
    # Затримка для 60 кадрів на секунду
    clock.tick(60)

# Завершуємо pygame
pygame.quit()
