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

    def _init_pygame(self):
        # Create window
        display_info = pygame.display.Info()
        self.screen_width = display_info.current_w
        self.screen_height = display_info.current_h
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height), flags=pygame.FULLSCREEN
        )
        print(f"Screen size: {self.screen_width}x{self.screen_height}")

        # Create clock
        self.clock = pygame.time.Clock()

    def _init_app_vars(self):
        self.done = False
        self.expression_name = DEFAULT_EXPRESSION
        self.current_expression_key = None
        self.max_expression_dims = get_closest_dimensions(
            self.screen_height, self.screen_height, EXPRESSION_ASPECT_RATIO
        )

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
        # Load expression image and scale to fit screen
        self.expression_img = pygame.image.load(
            os.path.join(EXPRESSION_FILE_PATH, f"{self.expression_name}.png")
        )
        self.expression_img = pygame.transform.scale(
            self.expression_img, self.max_expression_dims
        )

        # Put expression on screen
        self.screen.blit(
            self.expression_img, center_surface(self.screen, self.expression_img)
        )

    """ MAIN APP LOOP """

    def run(self):
        while not self.done:
            # Handle events
            self.handle_events()

            # Draw objects on screen
            self.screen.fill(BLACK)
            self.draw_expression()

            # Update display
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    app = App()
    app.run()
    pygame.quit()
