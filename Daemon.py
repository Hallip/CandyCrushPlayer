import pyautogui
import sys
from PIL import Image, ImageFilter
from Agent import Agent
import keyboard
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
    colors =[
            ((255, 165, 0), 'orange'), 
            ((0, 255, 255), 'aqua'), 
            ((0, 0, 0), 'black'), 
            ((0, 0, 255), 'blue'), 
            ((255, 0, 255), 'fuchsia'), 
            ((0, 128, 0), 'green'), 
            ((128, 128, 128), 'gray'), 
            ((0, 255, 0), 'lime'), 
            ((128, 0, 0), 'maroon'), 
            ((128, 0, 128), 'purple'), 
            ((255, 0, 0), 'red'), 
            ((255, 255, 255), 'white'), 
            ((255, 255, 0), 'yellow')
        ]
    for key, name in colors:
        r_c, g_c, b_c = key
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
    
    x_pos = [139, 208, 281, 352, 423, 493, 564, 635, 707]
    y_pos = [46, 110, 174, 238, 299, 362, 425, 491, 550]


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

            for x_add in range (-10,0):
                for y_add in range (-10,10):
                    pixel_color = image.getpixel((x+x_add, y+y_add))
                    colour_list.append(get_colour_name(pixel_color))
        
            colour_list = [elemento for elemento in colour_list if elemento != 'silver']
            colour_list = [elemento for elemento in colour_list if elemento != 'white']

            colour = elemento_mas_repetido(colour_list)

            if colour in ['lime','green','olive']:
                candy = 'G'
            elif colour in ['fuchsia','purple']:
                candy = 'P'
                
            elif colour in ['navy','aqua','blue']:
                candy = 'B'
            elif colour in ['yellow','orange']:
                
                x_add = 0
                y_add = 0
                pixel_color = image.getpixel((x+x_add, y+y_add))
                clr = get_colour_name(pixel_color)
                # print(row,col)
                # input(clr)
                if clr == 'yellow':
                    candy = 'Y'
                elif clr == 'orange':
                    candy = 'O'
                else:
                    candy = "U"
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
    y_pos = [46, 110, 174, 238, 299, 362, 425, 491, 550]
    
    pyautogui.click(x_pos[x], y_pos[y])
    
    # pyautogui.mouseDown()

    if (m == 'L'):
        pyautogui.click(x_pos[x-1], y_pos[y])

    if (m == 'R'):
        pyautogui.click(x_pos[x+1], y_pos[y])

    if (m == 'D'):
        pyautogui.click(x_pos[x], y_pos[y+1])
    
    if (m == 'U'):
        pyautogui.click(x_pos[x], y_pos[y-1])

    # pyautogui.mouseUp()
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
    if ((screenshot.getpixel((30, 34))) == (226, 225, 233)):
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
