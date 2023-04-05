import pygame


class TextBox(pygame.sprite.Sprite):
    def __init__(self, color, font="arial", value=0, size=(50, 50), font_size=24):
        """creates text ares for instruction and pause screen

        Args:
            color (rgb): color of the text
            font (str, optional): font of the text. Defaults to "arial".
            value (int, optional): the text of the text box. Defaults to 0.
            size (tuple, optional): size of the text box. Defaults to (50, 50).
            font_size (int, optional): size of the text. Defaults to 24.
        """
        super().__init__()
        self.value = value
        self.color = color
        pygame.font.init()
        self.image = pygame.Surface(size)
        self.font = pygame.font.SysFont(font, font_size)
        self.rect = self.image.get_rect()

    def update(self):
        font_surface = self.font.render(str(self.value), True, self.color)
        self.image.fill((110,139,61))
        self.image.blit(font_surface, (0, 0))
