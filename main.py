import pygame
import sys
import time


from sprites.Space import Space
from sprites.spaceship import Spaceship
from sprites.menus import Button
from sprites.menus import TextBox
from sprites.alien import Alien, generate_aliens
import sprites.options as options
from sprites.explosion import Explotion
import sprites.scores as score

pygame.init()

# Constants
WIDTH = 600
HEIGHT = 700
FPS = 60

# Creating Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

# Game Variables
cooldown = 500
scores = score.score_load()["scores"]
start_time = time.perf_counter()


def main():
    options_data = options.options_load()
    # Sprites
    space = Space()
    player_bullets = pygame.sprite.Group()
    player = Spaceship(player_bullets, cooldown, options_data['volume_shot'])
    aliens = pygame.sprite.Group()
    aliens_bullets = pygame.sprite.Group()
    generate_aliens(aliens, aliens_bullets)
    explosions = pygame.sprite.Group()
    # Game Loop
    running = True
    while running:
        # Refresh Rate
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                menu()

        for alien in aliens.sprites():
            if pygame.sprite.spritecollide(alien, player_bullets, True, pygame.sprite.collide_mask):
                explosion = Explotion(alien.rect.center)
                explosions.add(explosion)
                explosion.sound.play()
                alien.kill()
                explosion.draw(screen)
                explosion.update()
        if pygame.sprite.spritecollide(player, aliens_bullets, True, pygame.sprite.collide_mask):
            explosion = Explotion(player.rect.center)
            explosion.sound.play()
            explosions.add(explosion)
            player.kill()
            # Score Save
            end_time = time.perf_counter()
            scores.append(end_time-start_time)
            score.score_save(scores)
            static = pygame.image.load(r"assets/images/Static.png")
            tick = 0
            while tick < 100:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.get_surface().blit(static, static.get_rect())
                pygame.display.update()
                tick += 1


            menu()




        # Menu


        # Rendering
        screen.fill((0, 0, 0))
        space.draw(screen)
        player.draw(screen)
        player_bullets.draw(screen)
        aliens.draw(screen)
        explosions.draw(screen)
        aliens_bullets.draw(screen)






        # Updating Sprites
        space.update()
        player.update()
        player_bullets.update()
        aliens.update()
        explosions.update()
        aliens_bullets.update()






        # Updating Screen
        pygame.display.update()
def quit():
    scores.append("Victory")
    score.score_save(scores)
    pygame.quit()
    sys.exit()


def menu():
    global cooldown
    background = pygame.image.load(r"assets/images/main_background.jpeg")
    def cooldown_update():
        global cooldown
        cooldown = int(cooldown_box.text)
        main()
    # Sprites
    play_button = Button(screen.get_rect().centerx, screen.get_rect().centery - 50, 200, 50,
                    "Play Game", (150, 149, 149), (224, 222, 222), cooldown_update)
    titlebox = TextBox(screen.get_rect().centerx, 15,200, 50, "S P A C E  I N V A D E R S")
    cooldown_box = TextBox(play_button.rect.centerx, play_button.rect.centery + 30, 200, 50,
                           "500", "Bullet Cooldown(Change to number)")
    settings_button = Button(cooldown_box.rect.centerx, cooldown_box.rect.centery + 55, 200, 50,
                    "Settings", (150, 149, 149), (224, 222, 222), settings)
    quit_button = Button(settings_button.rect.centerx, settings_button.rect.centery + 55, 200, 50,
                    "Quit", (150, 149, 149), (224, 222, 222), quit)


    # Game Loop
    running = True
    while running:
        # Refresh Rate
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            cooldown_box.textupdate(event)

        # Menu

        # Rendering
        screen.fill((0,0,0))
        screen.blit(background, background.get_rect())
        play_button.draw(screen)
        quit_button.draw(screen)
        titlebox.draw(screen)
        cooldown_box.draw(screen)
        settings_button.draw(screen)



        # Updating Sprites
        play_button.handle_event(screen)
        quit_button.handle_event(screen)
        titlebox.update()
        cooldown_box.update()
        settings_button.handle_event(screen)







        # Updating Screen
        pygame.display.update()

def settings():
    global laser_volume
    options_data = options.options_load()
    background = pygame.image.load(r"assets/images/main_background.jpeg")
    def volume_update():
        options_data['volume_shot'] = int(laser_volume_box.text)/100
        options.options_save(options_data)
        menu()

    titlebox = TextBox(screen.get_rect().centerx, 15, 200, 50, "S E T T I N G S")
    play_button = Button(screen.get_rect().centerx, screen.get_rect().centery - 50, 200, 50,
                         "Play", (150, 149, 149), (224, 222, 222), volume_update)
    laser_volume_box_title = TextBox(play_button.rect.centerx, play_button.rect.centery + 35, 200, 50,
                               "Laser Shot Volume %", "Percentage of Laser Volume")

    laser_volume_box = TextBox(laser_volume_box_title.rect.centerx, laser_volume_box_title.rect.centery + 23, 200, 50,
                               str(int(options_data['volume_shot']*100)), "Percentage of Laser Volume")
    explosion_volume_box_title = TextBox(laser_volume_box.rect.centerx, laser_volume_box.rect.centery + 35, 200, 50,
                                     "Explosion Shot Volume %", "Percentage of Explosion Volume")

    explosion_volume_box = TextBox(explosion_volume_box_title.rect.centerx, explosion_volume_box_title.rect.centery + 23, 200, 50,
                               str(int(options_data['volume_explosion'] * 100)), "Percentage of Explosion Volume")

    # Game Loop
    running = True
    while running:
        # Refresh Rate
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            laser_volume_box.textupdate(event)

        # Menu

        # Rendering
        screen.fill((0, 0, 0))
        screen.blit(background, background.get_rect())
        play_button.draw(screen)
        laser_volume_box.draw(screen)
        titlebox.draw(screen)
        laser_volume_box_title.draw(screen)
        explosion_volume_box_title.draw(screen)
        explosion_volume_box.draw(screen)






        # Updating Sprites
        play_button.handle_event(screen)
        laser_volume_box.update()
        titlebox.update()
        laser_volume_box_title.update()
        explosion_volume_box.update()
        explosion_volume_box_title.update()






        # Updating Screen
        pygame.display.update()





if __name__ == "__main__":
    menu()




