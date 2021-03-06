# -*- coding: utf-8 -*-
import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch
from scipy import misc
from PIL import Image
import numpy as np
import pickle
import time

def main():

    # loading astronaut image
    # img = skimage.data.coffee()
    img = np.asarray(Image.open('berlin2.jpg'))

    # perform selective search
    img_lbl, regions = selectivesearch.selective_search(
        img, scale=700, sigma=0.8, min_size=10)

    candidates = set()
    for r in regions:
        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            continue
        # excluding regions smaller than 2000 pixels
        if r['size'] < 800:
             continue
        # distorted rects
        x, y, w, h = r['rect']
        # if w / h > 1.2 or h / w > 1.2:
        #     continue
        candidates.add(r['rect'])

    # draw rectangles on the original image
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    f = open(time.ctime(),'wr')
    pickle.dump(candidates,f);
    f.close()

    # ax.imshow(img)
    # for x, y, w, h in candidates:
    #     print x, y, w, h
    #     rect = mpatches.Rectangle(
    #         (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
    #     ax.add_patch(rect)

    # plt.show()
    # ax.imsave("test.jpg")

if __name__ == "__main__":
    main()
