import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def rotacion(ruta_imagen):
    imagen=Image.open(ruta_imagen).convert("L")
    imagen=np.array(imagen)
    dimensiones=np.shape(imagen)
    imagen_rotada=[]
    imagen_volteada=[]
    filas=dimensiones[0]
    colum=dimensiones[1]
    #Rotacion 90°
    for j in range(colum):
        nueva_fila=[]
        for i in range(filas-1,-1,-1):
            nueva_fila.append(imagen[i][j])
        imagen_rotada.append(nueva_fila)
     
    #Rotacion 180° 
    for i in range(filas - 1, -1, -1):
        nueva_fila = []
        for j in range(colum - 1, -1, -1):
            nueva_fila.append(imagen[i][j])
        imagen_volteada.append(nueva_fila)
    plt.imshow(imagen, cmap="grey")
    plt.show()
    plt.imshow(imagen_rotada, cmap="grey")
    plt.show()
    plt.imshow(imagen_volteada, cmap="grey")
    plt.show()

rotacion("zenith.jpg")
