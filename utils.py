import pygame


# Calculate the closest dimensions to fit a target aspect ratio
def get_closest_dimensions(width: int, height: int, target_ratio: tuple):
    # Calculate aspect ratios
    target_ratio = target_ratio[0] / target_ratio[1]
    current_ratio = width / height

    # Reduce dimensions to fit target aspect ratio
    if current_ratio > target_ratio:
        # Keep height, reduce width (landscape)
        width = int(height * target_ratio)
    elif current_ratio < target_ratio:
        # Keep width, reduce height (portrait)
        height = int(width / target_ratio)

    return width, height


# Center a surface within a master surface
def center_surface(master: pygame.Surface, surface: pygame.Surface):
    center_x = (master.get_width() - surface.get_width()) // 2
    center_y = (master.get_height() - surface.get_height()) // 2
    return center_x, center_y
