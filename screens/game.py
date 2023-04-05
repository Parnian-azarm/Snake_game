import pygame
from components.final import *
from .base_screen import BaseScreen


class GameScreen(BaseScreen):
    def __init__(self, window):
        """The game screen has a snake that moves, and a score box and a health box
        all other classes initiates here.
        """
        super().__init__(window)
        self.window = window
        self.snake = Snake(self.window)
        self.snake.draw()

        self.red = RedApple(self.window)
        self.redapple = pygame.sprite.Group()
        self.redapple.add(self.red)

        self.bonus = Bonus(self.window)
        self.rabbit = pygame.sprite.Group()
        self.rabbit.add(self.bonus)

        self.green = GreenApple(self.window)
        self.greenapple = pygame.sprite.Group()
        self.greenapple.add(self.green)
    

    def restart(self):
        """resets the game when the game is over
        """
        self.snake.tail = self.snake.tail
        self.snake.health = 3
        self.snake.point = 0
        self.snake.no = pygame.time.get_ticks() /1000
        self.snake.tail = TailGroup()
        self.snake.wall = False
        self.snake.speed = 250
        self.pause = False

    def update(self):
        """Deal with colides of the snakes head with different objects (red apple, green apple, rabbit, tail, wall)
        as green apple appear since game is initiated, we want to count the points and appear on screen once snake tail length
        is greater than 2.
        """
        if pygame.sprite.spritecollideany(self.snake, self.redapple):
            self.snake.point += 1
            self.red.kill()
            self.snake.grow()
            self.snake.draw()
            self.snake.speed -=10
            self.red = RedApple(self.window)
            self.redapple.add(self.red)

            self.green.kill()
            self.green = GreenApple(self.window)
            self.greenapple.add(self.green)

            if self.snake.point == 4 or self.snake.point == 7 or self.snake.point == 9:
                self.bonus.kill()
                self.bonus = Bonus(self.window)
                self.rabbit.add(self.bonus)        

        if self.snake.point == 4 or self.snake.point == 7 or self.snake.point == 9:
            if pygame.sprite.spritecollideany(self.snake, self.rabbit):
                self.snake.point += 3
                self.bonus.kill()
                self.bonus = Bonus(self.window)
                self.rabbit.add(self.bonus)

                self.red.kill()
                self.red = RedApple(self.window)
                self.redapple.add(self.red)

                self.green.kill()
                self.green = GreenApple(self.window)
                self.greenapple.add(self.green)


        if len(self.snake.tail) > 2:
            if pygame.sprite.spritecollide(self.snake, self.greenapple, dokill=True):
                self.snake.health -= 1
                self.green.kill()
                self.snake.speed -=10
                self.green = GreenApple(self.window)
                self.greenapple.add(self.green)

                self.red.kill()
                self.red = RedApple(self.window)
                self.redapple.add(self.red)

                if self.snake.point == 4 or self.snake.point == 7 or self.snake.point == 9:
                    self.bonus.kill()
                    self.bonus = Bonus(self.window)
                    self.rabbit.add(self.bonus)


        self.snake.move(self.snake.direction)      
        self.persistent["game_point"] = self.snake.point
        self.persistent["health"] = self.snake.health

        if pygame.sprite.spritecollideany(self.snake, self.snake.tail):
            self.restart()
            print("you lost")
            self.running = False
            pygame.display.set_caption("Game Over Screen")
            self.next_screen = "game_over"

        if self.snake.health == 0 :
            self.restart()
            print("you lost")
            self.running = False
            pygame.display.set_caption("Game Over Screen")
            self.next_screen = "game_over"

        if self.snake.wall == True:
            self.restart()
            print("you lost")
            self.running = False
            pygame.display.set_caption("Game Over Screen")
            self.next_screen = "game_over"

        
    def draw(self):
        """Draw the game screen. rabbit only appear on screen when snake point is 4,7, and 9."""
        self.snake.draw()
        self.redapple.draw(self.window)

        if self.snake.point == 4 or self.snake.point == 7 or self.snake.point == 9:
            self.rabbit.draw(self.window)
        if len(self.snake.tail) > 2:
            self.greenapple.draw(self.window)


    def manage_event(self, event):
        """
        Event management for the game screen.
        Pressing space  pauses the game.
        Pressing arrows moves the snake.
        """

        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.snake.pause = True
                self.pa = True
                self.running = False
                pygame.display.set_caption("Pause Screen")
                self.next_screen = "pause"
            if event.key == pygame.K_LEFT:
                if self.snake.direction != "right":
                    self.snake.move("left")
            elif event.key == pygame.K_RIGHT:
                if self.snake.direction != "left":
                    self.snake.move("right")
            elif event.key == pygame.K_UP:
                if self.snake.direction != "down":
                    self.snake.move("up")
            elif event.key == pygame.K_DOWN:
                if self.snake.direction != "up":
                    self.snake.move("down")


