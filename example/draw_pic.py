# -*- coding: utf-8 -*-
import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import misc
from PIL import Image
import numpy as np

img = np.asarray(Image.open('berlin.jpg'))

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
ax.imshow(img)


with open('berlin_list.txt') as f:
    for line in f.readlines():
        nums = [int(item) for item in line.split()]
        rect = mpatches.Rectangle((nums[0], nums[1]), nums[2], nums[3], fill=False, edgecolor='red', linewidth=1)
        ax.add_patch(rect)


plt.show()






# rect = mpatches.Rectangle((4541, 4298), 946, 1607, fill=False, edgecolor='red', linewidth=1)
# ax.add_patch(rect)
# plt.show()
