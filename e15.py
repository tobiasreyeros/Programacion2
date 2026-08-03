import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

imagen_original = Image.open('zenith.jpg')

imagen_gris_pil = imagen_original.convert('L')

array_gris = np.array(imagen_gris_pil)

filas=len(array_gris)
columnas=len(array_gris[0])
for i in range(filas):
    for j in range(columnas // 2):
        aux = array_gris[i][j]

        indice_derecho = columnas - 1 - j

        array_gris[i][j] = array_gris[i][indice_derecho]
        array_gris[i][indice_derecho] = aux
imagen_final = Image.fromarray(array_gris)

plt.imshow(imagen_final, cmap='gray')
plt.show()
