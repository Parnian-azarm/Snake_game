import pygame

from components import Button

from .base_screen import BaseScreen


class WelcomeScreen(BaseScreen):
    def __init__(self, window):
        """
        Creates two buttons on the screen.
        Play gets you to game screen
        Help gets you to rules screen to see the instructions of the game
        """
        pygame.display.set_caption("Welcome Screen")
        super().__init__(window)
        self.sprites = pygame.sprite.Group()
        self.image = pygame.image.load("welcome_page-removebg-preview.png")
        self.s = pygame.transform.scale(self.image, (600 ,400))

        self.button1 = Button(250, 80, "Play")
        self.button1.rect.x = 30
        self.button1.rect.y = 500

        self.button2 = Button(250, 80, "Help")
        self.button2.rect.x = 320
        self.button2.rect.y = 500

        self.sprites.add(self.button1, self.button2)


    def draw(self):
        """Draws the screen"""
        self.window.fill((110,139,61))
        self.window.blit(self.s, (0,15))
        self.sprites.draw(self.window)


    def manage_event(self, event):
        """Event management for pause screen 
        Clicking game get's you to game screen
        Clicking Help gets you to rules screen
        """
        if event.type == pygame.QUIT:
            self.ruuning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button1.rect.collidepoint(event.pos) :
                self.running = False
                pygame.display.set_caption("Game Screen")
                self.next_screen = "game"

            if self.button2.rect.collidepoint(event.pos) :
                self.running = False
                pygame.display.set_caption("Help Screen")
                self.next_screen = "rule"
 
