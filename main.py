import pygame


# Main logic
def main(screen: curses.window):

    print(f"Terminal size: {WIDTH}x{HEIGHT} --> Aspect Ratio: {WIDTH / HEIGHT:.3f}")

    target_width, target_height = get_closest_aspect_ratio(WIDTH, HEIGHT)
