import pygame


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, bullets, cooldown, laser_volume = 0.1):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/spaceship.png")
        self.rect = self.image.get_rect()
        self.bullets = bullets
        self.cooldown = cooldown
        self.last_shot = pygame.time.get_ticks()
        self.shot_sound = pygame.mixer.Sound(r"assets/sounds/laser.wav")
        self.shot_sound.set_volume(laser_volume)

        surface = pygame.display.get_surface()

        self.rect.centerx = surface.get_rect().centerx
        self.rect.bottom = surface.get_rect().bottom




    def update(self):
        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.rect.x > 0:
            self.rect.x -= 3
        if (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.rect.right < pygame.display.get_surface().get_width():
            self.rect.x += 3
        if (key[pygame.K_UP] or key[pygame.K_w]) and self.rect.y > pygame.display.get_surface().get_height() * 0.667:
            self.rect.y -= 3
        if (key[pygame.K_DOWN] or key[pygame.K_s]) and self.rect.bottom != pygame.display.get_surface().get_rect().bottom:
            self.rect.y += 3
        now = pygame.time.get_ticks()
        if (key[pygame.K_SPACE]) and now - self.last_shot > self.cooldown:
            bullet = Bullet(self.rect.midtop, self.cooldown)
            self.bullets.add(bullet)
            self.last_shot = now
            self.shot_sound.play()





    def draw(self, surface):
        surface.blit(self.image, self.rect)




class Bullet(pygame.sprite.Sprite):
    def __init__(self, coodrinates, cooldown):
        super().__init__()
        self.image = pygame.image.load(r"assets/images/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = coodrinates
        self.cooldown = cooldown



    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()


    def draw(self, surface):
        surface.blit(self.image, self.rect)

