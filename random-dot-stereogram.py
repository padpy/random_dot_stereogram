import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

left_image = np.random.choice((0,1), size=(150, 100))
right_image = np.copy(left_image)

aoi = np.copy(right_image[70:80, 45:55])
right_image[70:80, 45:55] = np.random.choice((0,1), size=(10, 10))
right_image[68:78, 43:53] = aoi

full_image = np.hstack( (np.ones((150, 5)), left_image, np.ones((150, 5)), right_image, np.ones((150, 5))) )
full_image = np.vstack( (np.ones((5, full_image.shape[1])), full_image, np.ones((5, full_image.shape[1]))) )
# plt.imshow(full_image, cmap='gray')
# plt.show()

Image.fromarray(full_image.astype(np.uint8)*255).save('random-dot-stereogram.png', 'PNG')