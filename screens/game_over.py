import pygame

from components import Button, TextBox

from .base_screen import BaseScreen


class GameOverScreen(BaseScreen):
    def __init__(self, window):
        """
        The game over screen has two buttons and a textbox
        """
        super().__init__(window)
        self.sprites = pygame.sprite.Group()
        self.image = pygame.image.load("dead-removebg-preview__2_-removebg-preview (1).png")
        self.s = pygame.transform.scale(self.image, (600 ,400))
        self.button1 = Button(250, 80, "Again")
        self.button1.rect.x = 30
        self.button1.rect.y = 500

        self.button2 = Button(250, 80, "Quit")
        self.button2.rect.x = 320
        self.button2.rect.y = 500

        self.textbox = TextBox((255, 0, 0), "comicsans", value="", size=(450, 50), font_size=30)
        self.textbox.rect.x = 30
        self.textbox.rect.y = 60

        self.textbox6 = TextBox((0, 0, 0), "comicsans", value="", size=(450, 30), font_size=25)
        self.textbox6.rect.x = 30
        self.textbox6.rect.y = 110
        
        self.sprites.add(self.button1, self.button2, self.textbox, self.textbox6)

    def update(self):
        """Updates the sprites based on the persistent data in the game"""
        self.textbox.value = "YOU DIED"
        self.textbox6.value = f"you lost with {self.persistent['game_point']} points"
        self.textbox.update()
        self.textbox6.update()
        
    def draw(self):
        """Draw the sprites"""
        self.window.fill((110,139,61))
        self.window.blit(self.s, (0,120))
        self.sprites.draw(self.window)

    def manage_event(self, event):
        """Go back to the welcome screen if we click button 1"""  
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = False
            if self.button1.rect.collidepoint(event.pos):
                pygame.display.set_caption("Welcome Screen")
                self.next_screen = "welcome"
            
            
