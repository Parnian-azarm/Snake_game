import pygame
from components import Button
from components.final import *
from .base_screen import BaseScreen


class RuleScreen(BaseScreen):
    def __init__(self, window):
        """the rule screen has instructions of the game and a back button to get you back to welcome page.
        """
        super().__init__(window)
        self.window = window
        self.sprites = pygame.sprite.Group()

        self.back = pygame.image.load("components/ins.jpg")
        self.s = pygame.transform.scale(self.back, (600,600))
        

        self.button1 = Button(600, 50, "Back")
        self.button1.rect.x = 0
        self.button1.rect.y = 550

        self.sprites.add(self.button1)


    def draw(self):
        """draws the help screen and the texts of the instructions 
        """
        self.window.blit(self.s, (0,0))
        self.window.blit(self.create_text_surface("Instructions", (0,0,0), "comicsans", 24), (20, 40))
        self.window.blit(self.create_text_surface("- Use arrow keys to move the snake", (0,0,0), "comicsans", 24), (20, 90))
        self.window.blit(self.create_text_surface("- You can pause the game by pressing SPACE", (0,0,0), "comicsans", 24), (20, 125))
        self.window.blit(self.create_text_surface("- Eat apple to get points", (0,0,0), "comicsans", 24), (20, 155))
        self.window.blit(self.create_text_surface("- Eating rabbits will give you 3 bonus point", (0,0,0), "comicsans", 24), (20, 185))
        self.window.blit(self.create_text_surface("- Be carefull with Green apples you loose health", (0,0,0), "comicsans", 24), (20, 215))
        self.window.blit(self.create_text_surface("- You'll DIE if you loose all 3 healths", (0,0,0), "comicsans", 24), (20, 245))
        self.window.blit(self.create_text_surface("- Be carefull not to hit your tail", (0,0,0), "comicsans", 24), (20, 275))
        self.window.blit(self.create_text_surface("or you'll DIE", (0,0,0), "comicsans", 24), (35, 305))
        self.window.blit(self.create_text_surface("- Be carefull of walls after point 5", (0,0,0), "comicsans", 24), (20, 335))
        self.window.blit(self.create_text_surface("- If you hit the wall you'll DIE", (0,0,0), "comicsans", 24), (20, 365))
        self.sprites.draw(self.window)


    def manage_event(self, event):
        """Event management for rules screen 
        clicking back button gets you back to welcome screen
        """
        if event.type == pygame.QUIT:
            self.ruuning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button1.rect.collidepoint(event.pos) :
                self.running = False
                pygame.display.set_caption("Welcome Screen")
                self.next_screen = "welcome"