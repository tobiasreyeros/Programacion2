import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

imagen = Image.open("zenith.jpg").convert("L")
imagen = np.array(imagen, dtype=float)
fil, col = imagen.shape

K = np.array([[1, 2, 1],
              [2, 4, 2],
              [1, 2, 1]])

suma_kernel = np.sum(K)/16

filtrada = np.zeros((fil, col))

for i in range(1, fil - 1):
    for j in range(1, col - 1):
        submatriz = imagen[i-1:i+2, j-1:j+2]
        R = submatriz * K
        filtrada[i, j] = np.sum(R) / suma_kernel

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagen, cmap="grey")
plt.title("Original")

plt.subplot(1, 2, 2)
plt.imshow(filtrada, cmap="grey")
plt.title("Filtrada")

plt.show()
