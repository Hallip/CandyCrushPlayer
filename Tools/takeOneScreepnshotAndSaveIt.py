import pyautogui
from PIL import Image

#take screenshot
#screenshot = pyautogui.screenshot()
#screenshot = screenshot.resize((256, 144))
#screenshot.save("screenshot.png")



input_image_path = "Screenshot-default.png"
output_image_path = "machineVision.png"  # Adjust the output format if needed
image = Image.open(input_image_path)
#image= image.resize((256, 144))
# Define the 16-color palette (RGB values)
palette = [
    0, 0, 0,        # Black
    255, 255, 255,  # White
    255, 255, 0,    # yellow
    255, 0, 0,      # Red
    255, 43, 20,    # Secondary red
    0, 255, 0,      # Green
    39, 130, 0,     # Secondary Green
    66, 204, 7,     # 3 Gren
    0, 0, 255,      # Blue
    34, 155, 255,   # Secundary Blue
    128, 0, 128,    # Purple
    233, 67, 255,   # Scondary Purple
    255, 130, 6,    # Orange
    71, 90, 89      # Gray Background
    # Add more colors as needed
]



# Convert the palette list to an ImagePalette object
image_palette = Image.new("P", (1, 1))
image_palette.putpalette(palette)

# Convert the image to the specified palette
converted_image = image.convert("RGB").quantize(palette=image_palette)

# Save the converted image
converted_image= converted_image.resize((128, 128))

converted_image.save(output_image_path)