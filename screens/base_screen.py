import pygame
from components import final

class BaseScreen:
    """
    Base class for a screen. You should create your own classes that inherit from this class.
    """

    def __init__(self, window):
        """Default attributes"""
        self.window = window
        self.next_screen = False
        self.persistent = {}


    def run(self):
        """Runs the pygame event loop"""
        clock = pygame.time.Clock()
        self.running = True
        self.pa = False
        while self.running:
            clock.tick(60)
            self.update()
            self.draw()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.next_screen = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.next_screen = False
                self.manage_event(event)

    def create_text_surface(self, value, color, font, size=18):
        """generates text surface

        Args:
            value (string): the fint of the text
            color (rgb ): color of the text
            font (string): font of the text
            size (int, optional): size of the text. Defaults to 18.

        Returns:
            the text 
        """
        font = pygame.font.SysFont(font, size)
        text_surface = font.render(value, True, color)
  
        
        return text_surface

    @property
    def rect(self):
        return self.window.get_rect()

    def draw(self):
        """
        Override this method in your child classes to handle the draw operations for the screen.
        """
        pass

    def update(self):
        """
        Override this method in your child classes to handle the update operations for the screen.
        """
        pass

    def manage_event(self, event):
        """
        Override this method in your child classes to handle events for the screen.
        """
        pass
