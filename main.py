from constants import *
from utils import *
import pygame
import os

# Initialize Pygame
pygame.init()


class App:
    """INITIALIZATION FUNCTIONS"""

    def __init__(self):
        self._init_pygame()
        self._init_app_vars()
        self._init_expressions()
        self._init_keyboard()

    def _init_pygame(self):
        # Create window
        display_info = pygame.display.Info()
        self.screen_width = display_info.current_w
        self.screen_height = display_info.current_h
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height), flags=pygame.FULLSCREEN
        )

        # Create clock
        self.clock = pygame.time.Clock()

    def _init_app_vars(self):
        self.done = False
        self.expression_name = DEFAULT_EXPRESSION
        self.current_expression_key = None

    def _init_expressions(self):
        # Create surface for expressions with biggest 3x2 dimensions
        self.expr_width, self.expr_height = get_closest_dimensions(
            self.screen_width, self.screen_height, (3, 2)
        )
        self.expression = pygame.Surface((self.expr_width, self.expr_height))

    def _init_keyboard(self):
        pass

    """ APP HELPER FUNCTIONS """

    def handle_events(self):
        # Handle Pygame events
        for event in pygame.event.get():
            # Handle quit event
            if event.type == pygame.QUIT:
                self.done = True

            # Handle keydown event
            elif event.type == pygame.KEYDOWN:
                # Exit app on ESC key
                if event.key == pygame.K_ESCAPE:
                    self.done = True

                # Change expression on key press
                elif event.key in EXPRESSION_KEYMAP:
                    self.expression_name = EXPRESSION_KEYMAP[event.key]
                    self.current_expression_key = event.key

            # Handle keyup event
            elif event.type == pygame.KEYUP:
                if (
                    event.key in EXPRESSION_KEYMAP
                    and event.key == self.current_expression_key
                ):
                    # Default expression when key is released
                    self.expression_name = DEFAULT_EXPRESSION
                    self.current_expression_key = None

                    # Add slight delay to avoid rapid toggling
                    pygame.time.delay(EXPRESSION_SWITCH_DELAY)

    def draw_expression(self):
        # Load expression image
        self.expression_img = pygame.image.load(
            os.path.join(EXPRESSION_FILE_PATH, f"{self.expression_name}.png")
        )

        # Put image on expression surface
        self.expression.blit(
            pygame.transform.scale(
                self.expression_img, (self.expr_width, self.expr_height)
            ),
            (0, 0),
        )

        # Put expression surface on screen
        self.screen.blit(self.expression, center_surface(self.screen, self.expression))

    """ MAIN APP LOOP """

    def run(self):
        while not self.done:
            # Handle events
            self.handle_events()

            # Draw objects on screen
            self.screen.fill(BLACK)
            self.draw_expression()

            # Update display
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    app = App()
    app.run()
    pygame.quit()
