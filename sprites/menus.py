import pygame


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.font = pygame.font.Font(r"assets/fonts/pixelon.ttf", 36)
        self.rect.center = (x, y)

    def draw(self, surface):
        # Draw button with hover effect
        color = self.hover_color if self.rect.collidepoint(pygame.mouse.get_pos()) else self.color
        pygame.draw.rect(surface, color, self.rect)

        # Render and center text
        text_surface = self.font.render(self.text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        key = pygame.mouse.get_pressed()
        if key[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.action()

class TextBox:
    def __init__(self, x, y, width, height, text="500", placeholder = ""):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (211, 211, 211)
        self.text = text
        self.font = pygame.font.Font(r"assets/fonts/pixelon.ttf", 36)
        self.txt_surface = self.font.render(text, True, (255,255,255))
        self.active = False
        self.rect.midtop = (x,y)
        self.x = x
        self.y = y
        self.placehold = self.font.render(placeholder, True, (211,211,211))

    def textupdate(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, (255, 255, 255))

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        widthpla = max(200, self.placehold.get_width() + 10)
        if self.text == "":
            self.rect.width = widthpla
            self.rect.midtop = (self.x, self.y)
        else:
            self.rect.width = width
            self.rect.midtop = (self.x, self.y)

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        if self.text == "":
            screen.blit(self.placehold, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

