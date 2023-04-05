import pygame

from screens import GameOverScreen, GameScreen, WelcomeScreen, RuleScreen, PauseScreen


class App:
    """
    This is the main class for our application.
    It runs the "screens" and manages state (persistent data).
    """

    def __init__(self):
        """Creates a Pygame window"""
        self.window = pygame.display.set_mode((600, 600))
        self.persistent = {}

    def run(self):
        """
        This method runs the main loop, and switches between screens using the next_screen attribute.
        """
        screens = {
            "welcome": WelcomeScreen(self.window),
            "game": GameScreen(self.window),
            "rule": RuleScreen(self.window),
            "pause": PauseScreen(self.window),
            "game_over": GameOverScreen(self.window),
        }
        running = True
        current_screen = "welcome"
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Gets the screen instance to "run"
            screen = screens.get(current_screen)
            if not screen:
                raise RuntimeError(f"Screen {current_screen} not found!")

            # Updates the persistent data on the instance
            screen.persistent = self.persistent
            # Runs the main loop of the screen
            screen.run()
            # Exits the loop if necessary
            if screen.next_screen is False:
                running = False

            # Switch to the next screen and update the persistent data
            current_screen = screen.next_screen
            self.persistent = screen.persistent


if __name__ == "__main__":
    g = App()
    g.run()
