import webcolors
import keyboard
import pyautogui
import sys
from PIL import Image, ImageFilter

def reduce_color_palette(image):
    converted_image = image.filter(ImageFilter.MinFilter(1))
    # converted_image.show()
    return converted_image

def get_colour_name(rgb_triplet):
    min_colours = {}
    for key, name in webcolors.CSS21_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_triplet[0]) ** 2
        gd = (g_c - rgb_triplet[1]) ** 2
        bd = (b_c - rgb_triplet[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]




def codifyBoard(image):

    x_pos = [18, 28, 37, 47, 56, 65, 75, 84, 94]
    y_pos = [12, 20, 28, 37, 45, 54, 62, 71, 79]


    color_matrix = []

    for row in range(9):
        color_row = []
        for col in range(9):
            x = x_pos[col]
            y = y_pos[row]

            if row == 0 and col == 3:
                x = 44
                y = 12
                sys.stdout.flush()  
            pixel_color = image.getpixel((x, y))
            colour = get_colour_name(pixel_color)
            if colour in ['lime','green']:
                candy = 'G'
            elif colour == 'orange':
                candy = 'O'
            elif colour in ['fuchsia','purple']:
                candy = 'P'
            elif colour in ['navy','aqua','blue']:
                candy = 'B'
            elif colour == 'yellow':
                candy = 'Y'
            elif colour in ['maroon','red']:
                candy = 'R'
            else:
                candy = colour
            color_row.append(candy)
        color_matrix.append(color_row)
        
    return color_matrix


while True:
    if keyboard.is_pressed('e'):
        print("Tecla 'e' presionada. Saliendo del bucle.")
        break
    screenshot = pyautogui.screenshot()
    # screenshot = screenshot.resize((256, 144))
    # screenshot.save("screenshot.png")
    if ((screenshot.getpixel((30, 80))) == (226, 225, 233)):
        screenshot = screenshot.resize((256, 144))
        screenshot = reduce_color_palette(screenshot)
        board = (codifyBoard(screenshot))
        print(board)
        #save image
        screenshot.save("screenshot.png")

    sys.stdout.flush()  