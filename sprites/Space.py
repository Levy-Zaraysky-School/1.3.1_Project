import pygame



class Space(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/space.png")
        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load(r"assets/images/space.png")
        self.rect1 = self.image1.get_rect()

        surface = pygame.display.get_surface()
        self.rect.bottom = surface.get_rect().bottom
        self.rect1.bottom = self.rect.top

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)

    def update(self):
        self.rect.y += 5
        self.rect1.y += 5
        if self.rect.top >= pygame.display.get_surface().get_height():
            self.rect.bottom = self.rect1.top

        if self.rect1.top >= pygame.display.get_surface().get_height():
            self.rect1.bottom = self.rect.top
