import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Cargar la imagen y convertirla a escala de grises
imagen = Image.open("zenith.jpg").convert("L")
imagen = np.array(imagen, dtype=float)
fil, col = imagen.shape

# Kernel de desenfoque gaussiano 3x3
K = np.array([[1, 2, 1],
              [2, 4, 2],
              [1, 2, 1]])

# Suma de elementos del kernel para normalizar correctamente
suma_kernel = np.sum(K) # 16

# Crear matriz destino
filtrada = np.zeros((fil, col))

# Recorrido con ventana de 3x3
for i in range(1, fil - 1):
    for j in range(1, col - 1):
        submatriz = imagen[i-1:i+2, j-1:j+2]
        R = submatriz * K
        filtrada[i, j] = np.sum(R) / suma_kernel

# Visualización de los resultados
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagen, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(filtrada, cmap="gray")
plt.title("Filtrada (Desenfoque Gaussiano)")
plt.axis("off")

plt.show()