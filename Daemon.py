import pyautogui
import sys
from PIL import Image



def getCandy(color):
    color = color - 11

    x,y = color%6,int(color/6)

    if (y == 0 and x in range(1,5)):
        return("R")
    elif (y == 12 and x in range(1,5)):
        return("P")
    elif (y == 12 and x in range(1,5)):
        return("P")

def reduce_color_palette(image, colors=256):
    reduced_image = image.convert("P", palette="P", colors=colors)
    return reduced_image

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
            color_row.append(pixel_color)


        color_matrix.append(color_row)

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
        screenshot = reduce_color_palette(screenshot, colors=128)
        print((codifyBoard(screenshot)))
    sys.stdout.flush()  

# Guardar imagen.
#screenshot.save("screenshot.png")