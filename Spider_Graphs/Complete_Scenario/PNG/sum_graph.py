import numpy as np
import matplotlib.pyplot as plt

w = 30
h = 30
fig = plt.figure(figsize=(25, 25))
columns = 4
rows = 2
#read png files from a folder

img_AzIv = plt.imread('Calenda_Complete.png')
img_FdI = plt.imread('Meloni_Complete.png')
img_FI = plt.imread('Berlusconi_Complete.png')
img_L = plt.imread('Salvini_Complete.png')
img_M5S = plt.imread('Conte_Complete.png')
img_PD = plt.imread('Letta_Complete.png')
img_pE = plt.imread('Bonino_Complete.png')
img_SiVe = plt.imread('Fratoianni_Complete.png')

images = [img_AzIv, img_FdI, img_FI, img_L, img_M5S, img_PD, img_pE, img_SiVe]
parties = ['Calenda', 'Meloni', 'Berlusconi', 'Salvini', 'Conte', 'Letta', 'Bonino', 'Fratoianni']
j = 0
for i in range(1, columns*rows +1):
    img = images[j]
    fig.add_subplot(rows, columns, i).set_title(str(parties[j]))
    #set off axis
    plt.axis('off')
    plt.imshow(img)
    j = j + 1
    if (j == 8):
        break
plt.show()
