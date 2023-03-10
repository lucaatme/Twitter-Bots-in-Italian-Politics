import numpy as np
import matplotlib.pyplot as plt

w = 30
h = 30
fig = plt.figure(figsize=(25, 25))
columns = 4
rows = 2
#read png files from a folder

img_AzIv = plt.imread('AzIv.png')
img_FdI = plt.imread('FdI.png')
img_FI = plt.imread('FI.png')
img_L = plt.imread('L.png')
img_M5S = plt.imread('M5S.png')
img_PD = plt.imread('PD.png')
img_pE = plt.imread('pE.png')
img_SiVe = plt.imread('SiVe.png')

images = [img_AzIv, img_FdI, img_FI, img_L, img_M5S, img_PD, img_pE, img_SiVe]
parties = ['AzIv', 'FdI', 'FI', 'L', 'M5S', 'PD', 'pE', 'SiVe']
j = 0
for i in range(1, columns*rows +1):
    img = images[j]
    fig.add_subplot(rows, columns, i).set_title('Party_'+str(parties[j]))
    #set off axis
    plt.axis('off')
    plt.imshow(img)
    j = j + 1
    if (j == 8):
        break
plt.show()
