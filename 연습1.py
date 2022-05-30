import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640,320))

running = True
while running:
    for pyEvent in pygame.event.get():
        print(pyEvent)
        if pyEvent.type == pygame.QUIT:
            running = False  

pygame.quit()
sys.exit()
