import random
import pygame

pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)

present_img = pygame.transform.scale(pygame.image.load('present.png'), (100, 100))
icon = pygame.transform.scale(pygame.image.load('Santa.png'), (32, 32))
sack_img = pygame.transform.scale(pygame.image.load('sack.png'), (200, 200))

pygame.display.set_icon(icon)


class Sack:
    def __init__(self):
        self.x = 500 / 2 - sack_img.get_rect().x / 2
        self.y = 500
        self.rect = sack_img.get_rect()
        self.rect.bottomleft = (self.x, self.y)


    def draw(self, surf):
        mouse = pygame.mouse.get_pos()[0]
        if mouse < 550 - self.rect.width / 2 and mouse + 50 > self.rect.width / 2:
            self.x = pygame.mouse.get_pos()[0] - (self.rect.width / 2)
        surf.blit(sack_img, (self.x, self.y))



class Present:
    def __init__(self, x, y=random.randint(0, 100)):
        self.x = x
        self.y = y
        self.kill = False
        self.rect = present_img.get_rect()
        self.rect.bottomleft = (self.x, self.y)

    def draw(self, win):
        if 0 < self.x and self.x < 500 - self.rect.width:
            pass
        else:
            self.kill = True

        win.blit(present_img, (self.x, self.y))

def display_score(score, win):
    score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
    win.blit(score_text, (win.get_width() - 150, 20))

def make_background():
    window_width = 500
    window_height = 700
    square_size = 50
    background = pygame.surface.Surface((500, 700))
    col1 = (0, 255, 255)
    col2 = (154, 211, 233)
    for row in range(0, window_height, square_size):
        for col in range(0, window_width, square_size):
            if (row // square_size + col // square_size) % 2 == 0:
                pygame.draw.rect(background, col1, (col, row, square_size, square_size))
            else:
                pygame.draw.rect(background, col2, (col, row, square_size, square_size))

    return background
def main(win):
    run = True
    score = 0
    clock = pygame.time.Clock()
    present_count = 0
    presents = []
    sack = Sack()
    while run:
        diff = score / 10 + 1
        clock.tick(60)
        win.blit(make_background(), (0, 0))
        display_score(score, win)

        if present_count < 3:
            present_count += 1
            presents.append(Present(random.randint(0, 500 - present_img.get_rect().x)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for present in presents:
            present.y += 1 * diff
            for i in range(len(presents)):
                if not present.rect.colliderect(presents[i]):
                    present.draw(win)
            if present.y > 700 or present.kill:
                presents.remove(present)
                present_count -= 1

        for present in presents:
            if (sack.x < present.x < sack.x + sack.rect.width) and (
                    present.y + present.rect.height > 700 - sack.rect.height + 70):
                score += 1
                presents.remove(present)
                present_count -= 1

        sack.draw(win)

        pygame.display.update()


if __name__ == '__main__':
    main(win)
