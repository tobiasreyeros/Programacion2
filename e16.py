import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def convertir_a_grises(imagen_rgb):
    """
    Convierte una imagen RGB a escala de grises usando la fórmula:
    Grises = R*0.2989 + G*0.5870 + B*0.1140
    """
    # Extraemos los canales (R, G, B)
    # imagen_rgb[:,:,0] es la matriz Roja, el 1 es Verde y el 2 es Azul
    r = imagen_rgb[:,:,0]
    g = imagen_rgb[:,:,1]
    b = imagen_rgb[:,:,2]
    
    # Aplicamos la fórmula proporcionada
    imagen_gris = r * 0.2989 + g * 0.5870 + b * 0.1140
    
    return imagen_gris

# 1. Importar la imagen a color
# Asegúrate de tener una imagen llamada 'imagen.jpg' en la misma carpeta
try:
    img_color = mpimg.imread('e16_imagen.jpg')
    
    # 2. Convertir la imagen usando nuestra función
    img_gris = convertir_a_grises(img_color)

    # 3. Mostrar los resultados
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Mostrar imagen original
    axes[0].imshow(img_color)
    axes[0].set_title("e16_imagen.jpg")
    axes[0].axis('off')

    # Mostrar imagen en grises
    # Usamos cmap='gray' para que Matplotlib sepa que debe interpretarlo como grises
    axes[1].imshow(img_gris, cmap='gray')
    axes[1].set_title("Imagen en Escala de Grises")
    axes[1].axis('off')

    plt.show()

except FileNotFoundError:
    print("Error: No se encontró el archivo 'imagen.jpg'. Por favor, verifica el nombre.")