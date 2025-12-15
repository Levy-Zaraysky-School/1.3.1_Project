import pygame


class Explotion(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()
        self.images = [r"assets/images/exp/exp{}.png".format(i) for i in range(1, 6)]
        self.index = 0
        self.image = pygame.image.load(self.images[self.index])
        self.sound = pygame.mixer.Sound(r"assets/sounds/explosion.wav")

        self.rect = self.image.get_rect()
        self.rect.center = coordinates

    def draw(self,surface):
        surface.blit(self.image, self.rect)


    def update(self):
        # Index Increases By One
        self.index += 1
        if self.index % 3 == 0:
            self.image = pygame.image.load(self.images[self.index // 3])
            print(self.index)


        if self.index // 3 >= len(self.images) - 1:
            self.kill()
