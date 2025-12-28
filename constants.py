import pygame

# Application Constants
FPS = 60

# Expression Constants
EXPRESSION_FILE_PATH = "expressions/"
EXPRESSION_SWITCH_DELAY = 200
DEFAULT_EXPRESSION = "neutral"
EXPRESSION_KEYMAP = {
    pygame.K_1: "happy",
    pygame.K_2: "sad",
    pygame.K_3: "angry",
    pygame.K_4: "surprised",
    pygame.K_5: "tired",
    pygame.K_6: "skeptical",
    pygame.K_7: "love",
    pygame.K_8: "broken",
}

# Colors
BLACK = (18, 18, 18)
LIGHT_GREY = (58, 58, 60)
DARK_GREY = (30, 30, 32)
WHITE = (255, 255, 255)
YELLOW = (185, 158, 25)
GREEN = (61, 143, 69)
