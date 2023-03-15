#plot two images in one figure
import matplotlib.pyplot as plt
import numpy as np

#read image
img1 = plt.imread('Bonino_Complete.png')
img2 = plt.imread('Bonino_NoBots.png')

#set figure size
plt.figure(figsize=(10,5))

#plot image and set title, set off axes
plt.subplot(1,2,1)
plt.imshow(img1)
plt.title('Complete Scenario Emma Bonino')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(img2)
plt.title('NoBots Scenario Emma Bonino')
plt.axis('off')

plt.show()