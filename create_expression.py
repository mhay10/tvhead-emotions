from PIL import Image
import argparse
import os


# Centers image at (x, y)
def center_image(x: int, y: int, image: Image.Image):
    return x - image.width // 2, y - image.height // 2


# Constants
SCREEN_WIDTH = 110
SCREEN_HEIGHT = 73
EYE_FILE_PATH = "eyes/"
EXPRESSION_OUTPUT_PATH = "expressions/"

# Set up argument parser
parser = argparse.ArgumentParser(description="Create screen images from a base image.")
parser.add_argument("left_eye", type=str, help="Name of left eye image")
parser.add_argument("right_eye", type=str, help="Name of right eye image")
parser.add_argument("expression_name", type=str, help="Name of the output expression.")
args = parser.parse_args()

# Load base images as greyscale
left = Image.open(os.path.join(EYE_FILE_PATH, f"{args.left_eye}.png")).convert("L")
right = Image.open(os.path.join(EYE_FILE_PATH, f"{args.right_eye}.png")).convert("L")

# Create image and paste eyes
expression = Image.new("L", (SCREEN_WIDTH, SCREEN_HEIGHT))
expression.paste(left, center_image(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, left))
expression.paste(right, center_image(SCREEN_WIDTH // 4 * 3, SCREEN_HEIGHT // 2, right))

# Save expression image
os.makedirs(EXPRESSION_OUTPUT_PATH, exist_ok=True)
expression.save(
    os.path.join(EXPRESSION_OUTPUT_PATH, f"{args.expression_name}.png"), format="PNG"
)
