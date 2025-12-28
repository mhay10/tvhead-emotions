# Calculate biggest dimensions fitting target aspect ratio
def get_closest_dimensions(width: int, height: int, target_dims: tuple = (3, 2)):
    # Calculate aspect ratios
    target_ratio = target_dims[0] / target_dims[1]
    current_ratio = width / height

    # Reduce dimensions to fit target aspect ratio
    if current_ratio > target_ratio:
        # Keep height, reduce width (landscape)
        width = int(height * target_ratio)
    elif current_ratio < target_ratio:
        # Keep width, reduce height (portrait)
        height = int(width / target_ratio)

    return width, height