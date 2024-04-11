import pygame

pygame.init()

# Screen
screen = pygame.display.set_mode([800, 600])
screen.fill("white")
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

# Define colors
colors = ["black", "red", "green", "blue", "yellow", "brown", "purple"]

# initial parameters
color = "black"
radius = 5
mode = "draw"  # 'draw', 'rectangle', 'circle', or 'erase'
drawing = False
start_pos = None


# Function to draw shapes
def draw_shape(screen, shape, color, start_pos, end_pos, radius):
    width = radius
    if shape == "rectangle":
        rect = pygame.Rect(
            start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
        )
        pygame.draw.rect(screen, color, rect, width)
    elif shape == "circle":
        center = start_pos
        radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
        pygame.draw.circle(screen, color, center, radius, width)
    elif shape == "erase":
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
            if mode in ["rectangle", "circle"]:
                draw_shape(screen, mode, color, start_pos, event.pos, radius=radius)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "draw":
                pygame.draw.circle(screen, color, event.pos, radius)
            elif mode == "erase":
                draw_shape(screen, "erase", color, start_pos, event.pos, radius)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_d:
                mode = "draw"
            elif event.key == pygame.K_e:
                mode = "erase"
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
            elif event.key == pygame.K_t:
                screen.fill("white")

    # FPS
    pygame.display.flip()
    clock.tick(60)

pygame.quit()