
# Import the Image class from Pillow
from PIL import Image

# Open the sample image
image = Image.open("sample.jpg")

# Display basic image information
print("Image format:", image.format)
print("Image dimensions:", image.size)
print("Image mode:", image.mode)

# Calculate the total number of pixels
width, height = image.size
total_pixels = width * height

print("Total pixels:", total_pixels)
# Read the color of the pixel at coordinate (0, 0)
pixel = image.getpixel((0, 0))

print("First pixel color:", pixel)