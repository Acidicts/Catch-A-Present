import pygame
from utils import Button
from game import make_background, icon, Present, main

pygame.init()
win = pygame.display.set_mode((500, 700))
pygame.display.set_caption('Santa\'s Sack')
pygame.display.set_icon(icon)
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 64)

start = Button(250, 250, pygame.transform.scale(pygame.image.load('start.png'), (200, 100)))
present = Present(200, 350)
quit = Button(250, 550, pygame.transform.scale(pygame.image.load('quit.png'), (200, 100)))
f = font.render("Santa's Sack", True, (255, 0, 0))

run = True
while run:
    win.blit(make_background(), (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if start.collision():
                main(win)
            if quit.collision():
                run = False

    win.blit(f, (250 - f.get_width() / 2, 100))
    start.update(win)
    present.draw(win)
    quit.update(win)

    pygame.display.update()

pygame.quit()
