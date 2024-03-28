import pygame
import datetime

pygame.init()
W, H = 1380, 1080
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mickey Mouse Clock")

mickey = pygame.image.load("imgs/mainclock.png")
second_hand = pygame.image.load("imgs/leftarm.png")
minute_hand = pygame.image.load("imgs/rightarm.png")

rect = mickey.get_rect(center=(W // 2, H // 2))

clock = pygame.time.Clock()
running = True

while running:
    screen.blit(mickey, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = datetime.datetime.now().time()
    second = current_time.second
    minute = current_time.minute

    left_angle = -(second * 6)
    rotate_left = pygame.transform.rotate(second_hand, left_angle)
    left_rect = rotate_left.get_rect(center = rect.center)
    screen.blit(rotate_left, left_rect.topleft)

    right_angle = -(minute * 6)
    rotate_right = pygame.transform.rotate(minute_hand, right_angle)
    right_rect = rotate_right.get_rect(center = rect.center)
    screen.blit(rotate_right, right_rect.topleft)
    pygame.display.flip()
    clock.tick(60)
