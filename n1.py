import pygame
from pygame.draw import *

pygame.init()

FPS = 30


screen = pygame.display.set_mode((400,400))
white = [255, 255, 255]
screen.fill(white)

circle(screen, (0, 0, 0), (200, 175), 151)
circle(screen, (255, 229, 0), (200, 175), 150)
circle(screen, (0, 0, 0), (140, 120), 31)
circle(screen, (0, 0, 0), (260, 120), 21)
circle(screen, (255, 0, 0), (140, 120), 30)

circle(screen, (255, 0, 0), (260, 120), 20)
circle(screen, (0, 0, 0), (140, 120), 15)
circle(screen, (0, 0, 0), (260, 120), 10)

rect(screen, (0, 0, 0), (120, 240, 170, 25))
pygame.draw.line(screen, (0, 0, 0), (180, 110), (70, 20), 25)

pygame.draw.line(screen, (0, 0, 0), (210, 105), (340, 85), 15)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
