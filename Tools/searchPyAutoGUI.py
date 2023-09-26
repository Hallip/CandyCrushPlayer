import pyautogui

# Captura la pantalla o región de interés
captura = pyautogui.screenshot(region=(0, 0, 1920, 1080))  # Ajusta las coordenadas y dimensiones según tu caso

# Guarda la imagen objetivo y cárgala
imagen_objetivo = './chocolate.png'

# Busca la imagen en la captura
ubicacion = pyautogui.locateOnScreen(imagen_objetivo, confidence=0.8)

# Si la imagen se encuentra, realiza una acción
if ubicacion is not None:
    x, y, ancho, alto = ubicacion
    centro_x = x + (ancho / 2)
    centro_y = y + (alto / 2)
    pyautogui.click(centro_x, centro_y)
    print("Se hizo clic en la imagen.")
else:
    print("No se encontró la imagen en la pantalla.")
