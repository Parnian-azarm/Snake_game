import pygame
from components import Button, TextBox
from components.final import *
from .base_screen import BaseScreen

class PauseScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        """the pause screen has the instructions and a back button to go back to welcome screen
        """
        self.window = window
        self.sprites = pygame.sprite.Group()

        self.back = pygame.image.load("components/wait-removebg-preview.png")
        self.s = pygame.transform.scale(self.back, (400,400))

        self.button = Button(250, 80, "RESUME")
        self.button.rect.x = 30
        self.button.rect.y = 500

        self.button2 = Button(250, 80, "QUIT")
        self.button2.rect.x = 320
        self.button2.rect.y = 500

        self.textbox = TextBox((0, 0, 0), "comicsans", value="", size=(200, 80), font_size=35)
        self.textbox.rect.x = 30
        self.textbox.rect.y = 60
        
        self.textbox2 = TextBox((0, 0, 0), "comicsans", value="", size=(200, 80), font_size=35)
        self.textbox2.rect.x = 30
        self.textbox2.rect.y = 150

        self.sprites.add(self.button, self.button2, self.textbox, self.textbox2)

    def update(self):
        """updates the textbox
        """
        self.textbox.value = f"Points: {self.persistent['game_point']}"
        self.textbox2.value = f"Health:{self.persistent['health']}"
        self.textbox.update()
        self.textbox2.update()
        

    def draw(self):
        """draws the screeen and the texts
        """
        self.window.fill((110,139,61))
        self.window.blit(self.s, (200,100))
        self.sprites.draw(self.window)

    def manage_event(self, event):
        """Event management for pause screen 
        clicking resume button gets you back to game screen
        clicking quit or pressing escape gets you out of the game
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = False

            if self.button.rect.collidepoint(event.pos) :
                self.pa = False
                pygame.display.set_caption("Game Screen")
                self.next_screen = "game"
            
            if self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = False