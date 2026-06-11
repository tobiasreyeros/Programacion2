import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

img = Image.open("e16_imagen")
matriz = np.array(img_g)
aux = 0

fyc = matriz.shape
row = fyc[0]
col = fyc[1]
mit = col//2

for i in range (row):
    for j in range(mit):
        aux = matriz [i][j]
        ind_con = -(j + 1)
        matriz[i][j] = matriz[i][ind_con]
        matriz[i][ind_con] = aux
        
plt.show()