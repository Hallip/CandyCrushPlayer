import pyautogui
import sys
from PIL import Image, ImageFilter


import matplotlib.pyplot as plt



def getCandy(color):

    r,g,b = color

    if (r > 200 and g < 10 and b < 10):
        return "R"
    if (r in range(20,60) and g in range(140,200) and b > 240):
        return "B"
    if (r > 250 and g in range(220, 250) and b < 30):
        return "Y"
    if (r > 250 and g in range(130, 160) and b < 50):
        return "O"    
    if (r in range(180, 210) and g in range(30, 50) and b > 250):
        return "P"  
    if (r in range(40, 100) and g in range(70, 210) and b < 50):
        return "G"  
    return color

def reduce_color_palette(image):
    converted_image = image.filter(ImageFilter.MinFilter(1))
    # converted_image.show()
    return converted_image

def codifyBoard(image):

    x_pos = [18, 28, 37, 47, 56, 65, 75, 84, 94]
    y_pos = [6, 14, 22, 31, 39, 48, 56, 65, 73]


    color_matrix = []

    for row in range(9):
        color_row = []
        for col in range(9):
            x = x_pos[col]
            y = y_pos[row]


            pixel_color = image.getpixel((x, y))
            # print(pixel_color)
            color_row.append(getCandy(pixel_color))


        color_matrix.append(color_row)

    color_matrix[0][3] = getCandy(image.getpixel((45, 5)))
    return color_matrix

def count_unique_elements(matrix):
    unique_elements = set()

    for row in matrix:
        for element in row:
            unique_elements.add(element)

    return len(unique_elements)

while True:
    screenshot = pyautogui.screenshot()
    if ((screenshot.getpixel((30, 40))) == (226, 225, 233)):
        screenshot = screenshot.resize((256, 144))
        screenshot = reduce_color_palette(screenshot)
        print((codifyBoard(screenshot)))
        #save image
        screenshot.save("screenshot.png")
    sys.stdout.flush()  

# Guardar imagen.
#screenshot.save("screenshot.png")