import pygame
import random

SCREEN_SIZE = (600, 600)

class TailBox(pygame.sprite.Sprite):
    def __init__(self):
        """creates a tail group for growing tail
        """
        super().__init__()
        self.image = pygame.Surface((25, 25))
        r = random.randint(0,255)
        b = random.randint(0,255)
        self.image.fill([r, 0, b])
        self.rect = self.image.get_rect()

class TailGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def grow(self, direction, head_rect):
        """Implements tail boxes

        Args:
            direction (string): gets the direction based on the key pressed for snake to move
            head_rect (cordinate): the cordinates of the head
        """
        box = TailBox()
        
        if len(self.sprites()):
            last_box = self.sprites()[-1]
            if direction == "right":
                box.rect.y = last_box.rect.y
                box.rect.right = last_box.rect.left
            elif direction == "left":
                box.rect.left = last_box.rect.right
                box.rect.y = last_box.rect.y
            elif direction == "up":
                box.rect.top = last_box.rect.bottom
                box.rect.x = last_box.rect.x
            elif direction == "down":
                box.rect.bottom = last_box.rect.top
                box.rect.x = last_box.rect.x
        
        else:
            if direction == "right":
                box.rect.y = head_rect.y
                box.rect.right = head_rect.left
            elif direction == "left":
                box.rect.y = head_rect.y
                box.rect.left = head_rect.right
            if direction == "up":
                box.rect.x = head_rect.x
                box.rect.top = head_rect.bottom
            elif direction == "down":
                box.rect.x = head_rect.x
                box.rect.bottom = head_rect.top
            
        self.add(box)


    def move(self, direction, head_rect):
        """moves the tail to follow head of the snake

        Args:
            direction (string): gets the direction based on the key pressed for snake to move
            head_rect (cordinate): the cordinates of the head
        """
        if not len(self.sprites()):
            return

        all = self.sprites()
        last = all[-1]
        but_last = all[:-1]

        self.empty()
        if direction == "right":
            last.rect.right = head_rect.left
            last.rect.y = head_rect.y
        if direction == "left":
            last.rect.left = head_rect.right
            last.rect.y = head_rect.y
        if direction == "up":
            last.rect.x = head_rect.x
            last.rect.top = head_rect.bottom
        if direction == "down":
            last.rect.x = head_rect.x
            last.rect.bottom = head_rect.top
        self.add(last)
        self.add(but_last)


class Snake(pygame.sprite.Sprite):
    def __init__(self, window):
        """generates the snakes head and initializes health and point of the game

        Args:
            window : the screen
        """
        self.length = 0
        self.window = window
        self.image = pygame.image.load("components/Untitled.png")
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.tail = TailGroup()
        self.direction = "up"
        self.health = 3
        self.point = 0
        self.no = pygame.time.get_ticks() /1000
        self.time = 0
        self.wall = False
        self.speed = 250
        self.pause = False


    def delay(self):
        """slows the movement of snake

        Returns:
            boolean: checks if we are making a delay
        """
        now = pygame.time.get_ticks()
        if now - self.time > self.speed:
            self.time = now
            return True
        else:
            return False

    def move(self, direction):
        """moves the snake's head

        Args:
            direction (string): gets the direction based on the key pressed for snake to move
        """
        self.direction = direction

        if self.delay():
            if self.direction == "up":    
                self.rect.y -= self.width

            elif self.direction == "down":  
                self.rect.y += self.width

            elif self.direction == "left":     
                self.rect.x -= self.width

            elif self.direction == "right":     
                self.rect.x += self.width
            
            self.tail.move(self.direction, self.rect)
        self.limitation()

    def limitation(self):
        """allows the snake to goes passed the screen and come back the other way
        and detects walls after it reachs point 4
        """
        if self.point < 4:
            if self.rect.right > SCREEN_SIZE[0]:
                self.rect.left = 0
            if self.rect.left < 0:
                self.rect.right = SCREEN_SIZE[0]
            if self.rect.top < 0:
                self.rect.bottom = SCREEN_SIZE[1]
            if self.rect.bottom > SCREEN_SIZE[1]:
                self.rect.top = 0

        else:
            if self.rect.right > SCREEN_SIZE[0] - 25:
                self.wall = True
            if self.rect.left < 25:
                self.wall = True
            if self.rect.top < 50:
                self.wall = True
            if self.rect.bottom > SCREEN_SIZE[1] - 25:
                self.wall = True


    def grow(self):
        """grows snake
        """
        self.tail.grow(self.direction, self.rect)

    def draw(self):
        """draws the game screen
        """
        self.window.fill((162,208,74))
        if self.point >= 4:
            self.back = pygame.image.load("components/baaaaaa-removebg-preview.png")
            self.s = pygame.transform.scale(self.back, (680,620))
            self.window.blit(self.s, (-40,-5))
        for x in range(0, SCREEN_SIZE[0], 25):
            pygame.draw.aaline(self.window, (162,208,74,255), (x, 0), (x, SCREEN_SIZE[0]), True)
        for y in range(0, SCREEN_SIZE[0], 25):
            pygame.draw.aaline(self.window, (162,208,74,255), (0, y), (SCREEN_SIZE[1], y), True)
        if self.point == 4 or self.point == 5:
            self.window.blit(self.create_text_surface("LEVEL 2 => Watch for Walls Now", (255, 0, 0)), (150, 50))
        self.window.blit(self.create_text_surface(f"points: {self.point}", (0, 0, 0)), (200, 5))
        self.window.blit(self.create_text_surface(f"health: {self.health}", (0, 0, 0)), (300, 5))
        self.window.blit(self.image, (self.rect.x, self.rect.y))
        self.tail.draw(self.window)


    def create_text_surface(self, value, color):
        """generates text surface

        Args:
            value (string): the fint of the text
            color (rgb ): color of the text

        Returns:
            the text box
        """
        default_font = pygame.font.get_default_font()
        font = pygame.font.Font(default_font, 18)
        text_surface = font.render(value, True, color)
        return text_surface



class RedApple(pygame.sprite.Sprite):
    base_image = pygame.image.load("components/red_apple-removebg-preview.png")
    def __init__(self, window):
        """creates red apple in randon positions

        Args:
            window : the screen
        """
        super().__init__()
        self.image = pygame.transform.scale(self.base_image, (25, 25))
        self.rect = pygame.rect.Rect([0, 0, 25-2, 25-2])
        self.rect.x = random.randint(25, (SCREEN_SIZE[0] - 65))
        self.rect.y = random.randint(50, (SCREEN_SIZE[1] - 35))
        self.window = window

class Bonus(pygame.sprite.Sprite):
    base_image = pygame.image.load("components/rabbibt.png")
    def __init__(self, window):
        """creates bonus (rabit) in random positions

        Args:
            window : the screen
        """
        super().__init__()
        self.image = pygame.transform.scale(self.base_image, (35, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(25, SCREEN_SIZE[0] - 65)
        self.rect.y = random.randint(50, SCREEN_SIZE[1] - 35)
        self.window = window

class GreenApple(pygame.sprite.Sprite):
    base_image = pygame.image.load("components/green_apple-removebg-preview.png")
    def __init__(self, window):
        """creates green apple in random positions 

        Args:
            window : the screen
        """
        super().__init__()
        self.window = window
        self.image = pygame.transform.scale(self.base_image, (30, 25))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(25, SCREEN_SIZE[0] - 65)
        self.rect.y = random.randint(50, SCREEN_SIZE[1] - 30)
        
        