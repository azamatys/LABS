import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 600))
running = True
x = 400
y = 300
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP] and y-25 > 0: y -= 20
    if pressed[pygame.K_DOWN] and y+25 < 600: y += 20
    if pressed[pygame.K_LEFT] and x-25 > 0: x -= 20
    if pressed[pygame.K_RIGHT] and x+25 < 1280: x += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()