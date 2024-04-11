import pygame
import math

# Инициализация Pygame
pygame.init()

# Создание экрана
screen = pygame.display.set_mode([800, 600])
screen.fill("white")
pygame.display.set_caption("Pygame Paint")
clock = pygame.time.Clock()

# Определение цветов
colors = ["black", "red", "green", "blue", "yellow", "brown", "purple"]

# Начальные параметры
color = "black"
radius = 5
mode = "draw"  # 'draw', 'rectangle', 'circle', or 'erase'
drawing = False
start_pos = None


# Функция для рисования форм
def draw_shape(screen, shape, color, start_pos, end_pos, radius):
    width = radius
    if shape == "rectangle":
        # Рисование прямоугольника
        length_x = end_pos[0] - start_pos[0]
        length_y = end_pos[1] - start_pos[1]
        if length_x < 0:
            length_x = abs(length_x)
            start_pos = (start_pos[0] - length_x, start_pos[1])
            rect = pygame.Rect(start_pos, (length_x, length_y))
        rect = pygame.Rect(start_pos, (length_x, length_y))
        pygame.draw.rect(screen, color, rect, width)
    elif shape == "circle":
        # Рисование круга
        center = start_pos
        radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
        pygame.draw.circle(screen, color, center, radius, width)
    elif shape == "square":
        # Рисование квадрата
        length = end_pos[0] - start_pos[0]

        if length < 0:
            length = abs(length)
            start_pos = (start_pos[0] - length, start_pos[1])
            rect = pygame.Rect(start_pos, (length, length))
        else:
            rect = pygame.Rect(start_pos, (length, length))
        pygame.draw.rect(screen, color, rect, width)
    elif shape == "right_triangle":
        # Рисование прямоугольного треугольника
        points = [start_pos, (start_pos[0], end_pos[1]), end_pos]
        pygame.draw.polygon(screen, color, points, width)
    elif shape == "equilateral_triangle":
        # Рисование равностороннего треугольника
        side_length = (end_pos[0] - start_pos[0]) * 2
        triangle_height = (math.sqrt(3) / 2) * side_length
        top_vertex = (start_pos[0], start_pos[1] - triangle_height / 2)
        left_vertex = (
            start_pos[0] - side_length / 2,
            start_pos[1] + triangle_height / 2,
        )
        right_vertex = (
            start_pos[0] + side_length / 2,
            start_pos[1] + triangle_height / 2,
        )
        points = (top_vertex, left_vertex, right_vertex)
        pygame.draw.polygon(screen, color, points, width)
    elif shape == "rhombus":
        # Рисование ромба
        mid_x = (start_pos[0] + end_pos[0]) // 2
        mid_y = (start_pos[1] + end_pos[1]) // 2
        points = [
            (mid_x, start_pos[1]),
            (end_pos[0], mid_y),
            (mid_x, end_pos[1]),
            (start_pos[0], mid_y),
        ]
        pygame.draw.polygon(screen, color, points, width)
    elif shape == "erase":
        # Стирание
        pygame.draw.rect(
            screen,
            "white",
            (end_pos[0] - radius, end_pos[1] - radius, radius * 2, radius * 2),
        )


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            if mode == "draw":
                pygame.draw.circle(screen, color, event.pos, radius)
            elif mode == "erase":
                draw_shape(screen, "erase", color, start_pos, event.pos, radius)

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode in [
                "rectangle",
                "circle",
                "square",
                "rhombus",
                "right_triangle",
                "equilateral_triangle",
            ]:
                draw_shape(screen, mode, color, start_pos, event.pos, radius=radius)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "draw":
                pygame.draw.circle(screen, color, event.pos, radius)
            elif mode == "erase":
                draw_shape(screen, "erase", color, start_pos, event.pos, radius)

        # Обработка клавиш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_d:
                mode = "draw"
            elif event.key == pygame.K_e:
                mode = "erase"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_h:
                mode = "rhombus"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_p:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_1:
                color = colors[0]
            elif event.key == pygame.K_2:
                color = colors[1]
            elif event.key == pygame.K_3:
                color = colors[2]
            elif event.key == pygame.K_4:
                color = colors[3]
            elif event.key == pygame.K_5:
                color = colors[4]
            elif event.key == pygame.K_6:
                color = colors[5]
            elif event.key == pygame.K_7:
                color = colors[6]
            elif event.key == pygame.K_UP:
                radius += 3
            elif event.key == pygame.K_DOWN:
                radius -= 3
            elif event.key == pygame.K_l:
                screen.fill("white")

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

pygame.quit()