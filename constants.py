import pygame

# Application Constants
FPS = 60

# Expression Constants
EXPRESSION_FILE_PATH = "expressions/"
EXPRESSION_ASPECT_RATIO = (3, 2)
EXPRESSION_IMG_WIDTH = 110
EXPRESSION_IMG_HEIGHT = 73
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
    pygame.K_8: "confused",
}

# Webserver Contants
WEBSERVER_HOST = "0.0.0.0"
WEBSERVER_PORT = 5000
WEBSERVER_API_USAGE_HTML = "./api_usage.html"

# Colors
BLACK = (0, 0, 0)
