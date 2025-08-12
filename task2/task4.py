from PIL import Image

# Load image
image = Image.open(
    r"C:\Users\eslamia\OneDrive\Pictures\Screenshots\Screenshot 2025-07-30 232802.png"
)  # dont forget to change path i didnt upload the image that i used as test
pixels = image.load()

width, height = image.size

# Loop over the left quarter and set pixels to black(0,0,0)
for x in range(width // 2):
    for y in range(height // 2):
        pixels[x, y] = (0, 0, 0)

# Save the modified image
image.save("output.png")
print("Image saved as output.png")
