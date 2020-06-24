import pygame
import random
pygame.init()

frstr = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Ploaie")

ceas = pygame.time.Clock()

nr = input("Numar de picaturi:")

class entit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800 - self.rect.width)
        self.rect.y = random.randrange(-40, -80, -40)
        self.vit = random.randrange(12, 18)
    def update(self):
        self.rect.y += self.vit
        if self.rect.y > 840:
            self.rect.x = random.randrange(0, 800 - self.rect.width)
            self.rect.y = random.randrange(-40, -80, -40)
            self.vit = random.randrange(12, 18)


particule = pygame.sprite.Group()
for i in range(int(nr)):
    monstr = entit()
    particule.add(monstr)

rulare = True
while rulare:
    ceas.tick(120)
    frstr.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rulare = False

    particule.update()
    particule.draw(frstr)
    pygame.display.flip()

pygame.quit()
