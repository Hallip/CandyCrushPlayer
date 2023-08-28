from PIL import Image, ImageDraw

# Define tu paleta personalizada (lista de colores RGB)
custom_palette = [(255, 255, 0),   # Amarillo
                  (0, 255, 0),     # Verde
                  (255, 0, 0),     # Rojo
                  (0, 0, 255),     # Azul
                  (128, 0, 128),   # Morado
                  (255, 128, 0),   # Naranja
                 ]

# Calcula el tamaño de la imagen basado en la cantidad de colores en la paleta
image_width = 50
image_height = len(custom_palette) * 50
image = Image.new("RGB", (image_width, image_height), "white")

# Crea un objeto ImageDraw para dibujar en la imagen
draw = ImageDraw.Draw(image)

# Dibuja los colores de la paleta en la imagen
for i, color in enumerate(custom_palette):
    y_start = i * 50
    y_end = (i + 1) * 50
    draw.rectangle([(0, y_start), (image_width, y_end)], fill=color)

# Guarda la imagen de la paleta
palette_image_path = "paleta_personalizada.png"
image.save(palette_image_path)

print("Imagen de paleta generada y guardada:", palette_image_path)
