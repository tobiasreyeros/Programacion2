import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def convertir_a_grises(ruta_imagen):
    #cargan la imagen en disco y la convierten
    #en una matriz tridimensional: alto, ancho, 3 canales(RGB)
    imagen_color = Image.open(ruta_imagen)
    array_color = np.array(imagen_color)
    alto = array_color.shape[0]
    ancho = array_color.shape[1]
    #crea una matriz vacia con las dimensiones
    #de la imagen (alto, ancho) de una sola
    #capa donde se guarda la intensidad de gris de cada pixel
    array_grises = np.zeros((alto, ancho))
                             
    #extrae los valores RGB del pixel en la posicion [i, j]
    for i in range(alto):
        for j in range(ancho):
            R = array_color[i, j, 0] 
            G = array_color[i, j, 1] 
            B = array_color[i, j, 2]
            #no se hace un promedio simple porque el
            #ojo humano no percibe todos los colores con el mismo brillo
            gris = (R * 0.2989) + (G * 0.5870) + (B * 0.1140)
            array_grises[i, j] = gris
    
    #crea un panel con 2 espacios para imagenes lado a lado.
    fig, ejes = plt.subplots(1, 2, figsize=(10, 5))
        
    ejes[0].imshow(array_color)
    #interpreta la matriz de un solo canal como escala de grises (negro = 0, blanco = 255).
    ejes[1].imshow(array_grises, cmap='gray')
    plt.tight_layout()
    plt.show()
    
convertir_a_grises("zenith.jpg")