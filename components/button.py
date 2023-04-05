import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, text, bgcolor=(0, 0, 0), fgcolor=(255, 255, 255)):
        """generates buttons

        Args:
            width (integer): _description_
            height (integer): _description_
            text (string): _description_
            bgcolor (tuple, optional): back ground color. Defaults to (0, 0, 0).
            fgcolor (tuple, optional): front ground color. Defaults to (255, 255, 255).
        """
        super().__init__()
        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.image = pygame.Surface((width, height))
        self.image.fill(bgcolor)
        text_surface = font.render(text, True, fgcolor)
        text_size = font.size(text)
        pos_x = (width - text_size[0]) / 2
        pos_y = (height - text_size[1]) / 2
        self.image.blit(text_surface, (pos_x, pos_y))
        self.rect = self.image.get_rect()
