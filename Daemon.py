import pyautogui
import sys
from PIL import Image, ImageFilter
from Agent import Agent
import keyboard
import webcolors
import time
from collections import Counter


# def getCandy(color):

#     r,g,b = color

#     if (r > 200 and g < 130 and b < 50):
#         return "R"
#     if (r in range(20,100) and g in range(100,220) and b > 150):
#         return "B"   
#     if (r > 240 and g in range(200, 250) and b < 110):
#         return "Y"
#     if (r > 240 and g in range(130, 200) and b < 120):
#         return "O"    
#     if (r in range(180, 240) and g in range(30, 180) and b > 240):
#         return "P"  
#     if (r in range(40, 160) and g in range(70, 255) and b < 130):
#         return "G"  
#     return color

def elemento_mas_repetido(arreglo):
    if len(arreglo) == 0:
        return "Gray"
    contador = Counter(arreglo)
    elemento, repeticiones = contador.most_common(1)[0]
    return elemento

def get_colour_name(rgb_triplet):
    min_colours = {}
    for key, name in webcolors.CSS21_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_triplet[0]) ** 2
        gd = (g_c - rgb_triplet[1]) ** 2
        bd = (b_c - rgb_triplet[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]



# def reduce_color_palette(image):
#     converted_image = image.filter(ImageFilter.MinFilter(1))
#     # converted_image.show()
#     return converted_image

def codifyBoard(image):


    x_pos = [139, 210, 281, 352, 423, 493, 565, 636, 707]
    y_pos = [92, 156, 220, 284, 345, 408, 471, 537, 596]


    color_matrix = []

    for row in range(9):
        color_row = []
        for col in range(9):
            x = x_pos[col]
            y = y_pos[row]

            colour_list = []

            if row == 0 and col == 3:
                x = 344
                y = 92

            else: 

                pixel_color = image.getpixel((x+5, y))
                colour_list.append(get_colour_name(pixel_color))
                pixel_color = image.getpixel((x+5, y-5))
                colour_list.append(get_colour_name(pixel_color))
                pixel_color = image.getpixel((x+5, y+5))
                colour_list.append(get_colour_name(pixel_color))

            pixel_color = image.getpixel((x, y))
            colour_list.append(get_colour_name(pixel_color))
            
            pixel_color = image.getpixel((x-5, y))
            colour_list.append(get_colour_name(pixel_color))

            pixel_color = image.getpixel((x, y+5))
            colour_list.append(get_colour_name(pixel_color))

            pixel_color = image.getpixel((x, y-5))
            colour_list.append(get_colour_name(pixel_color))

            pixel_color = image.getpixel((x-5, y-5))
            colour_list.append(get_colour_name(pixel_color))
            
            pixel_color = image.getpixel((x-5, y+5))
            colour_list.append(get_colour_name(pixel_color))

            colour_list = [elemento for elemento in colour_list if elemento != 'silver']
            colour_list = [elemento for elemento in colour_list if elemento != 'white']

            colour = elemento_mas_repetido(colour_list)

            if colour in ['lime','green','olive']:
                candy = 'G'
            elif colour == 'orange':
                candy = 'O'
            elif colour in ['fuchsia','purple']:
                candy = 'P'
            elif colour in ['navy','aqua','blue']:
                candy = 'B'
            elif colour == 'yellow':
                candy = 'Y'
            elif colour in ['red']:
                candy = 'R'
            elif colour in ['maroon']:
                candy = 'C'
            else:
                candy = colour
            # if 'white' in colour_list:
            #     candy = candy.lowercase()
            color_row.append(candy)
        color_matrix.append(color_row)
        
    return color_matrix

# def count_unique_elements(matrix):
#     unique_elements = set()

#     for row in matrix:
#         for element in row:
#             unique_elements.add(element)

#     return len(unique_elements)

def actuador(movimiento):
    x, y, m, score, code =  movimiento

    x_pos = [139, 210, 281, 352, 423, 493, 565, 636, 707]
    y_pos = [92, 156, 220, 284, 345, 408, 471, 537, 596]
    
    pyautogui.moveTo(x_pos[x], y_pos[y], duration=0.0)
    
    pyautogui.mouseDown()

    if (m == 'L'):
        pyautogui.moveTo(x_pos[x-1], y_pos[y], duration=0.05)

    if (m == 'R'):
        pyautogui.moveTo(x_pos[x+1], y_pos[y], duration=0.05)

    if (m == 'D'):
        pyautogui.moveTo(x_pos[x], y_pos[y+1], duration=0.05)
    
    if (m == 'U'):
        pyautogui.moveTo(x_pos[x], y_pos[y-1], duration=0.05)

    pyautogui.mouseUp()
    # pyautogui.moveTo(110, 10, duration=0.1)


myAgent = Agent()

consecutive_plays = 0
lastPlay = ""

while True:

    if keyboard.is_pressed('e'):
        break
    screenshot = pyautogui.screenshot()
    # screenshot = screenshot.resize((256, 144))
    # screenshot.save("screenshot.png")
    if ((screenshot.getpixel((30, 80))) == (226, 225, 233)):
        # screenshot = screenshot.resize((256, 144))
        # screenshot = reduce_color_palette(screenshot)
        board = (codifyBoard(screenshot))
        if (consecutive_plays >= 3):
            x, y, m, score, code =  lastPlay
            board[y][x] = "I"
            print ("indefinido")
        
        print(board)
        #save image
        screenshot.save("screenshot.png")
        


        movement = myAgent.calcularMovimientos(board)
        # print (movement)
        actuador(movement)
        if (lastPlay != movement):
            consecutive_plays = 0
        else:
            consecutive_plays+=1
        lastPlay = movement
    sys.stdout.flush()  


# Guardar imagen.
#screenshot.save("screenshot.png")