# snippet_19a.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Multi-level Thresholding.

"""

import cv2
import sys
import numpy as np



#############################################################
## The main 'function'
##
if __name__ == '__main__':

    # Open image as greyscale
    input_file = 'panda.png'
    img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
    #
    # Check for success
    if img is None:
        print('Failed to open', input_file)
        sys.exit()

    # Perform Muti-level Thresholding
    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            if img[r, c] >= 0 and img[r, c] < 48:
                img[r, c] = (0+48)/2
            elif img[r, c] >= 48 and img[r, c] < 128:
                img[r, c] = (48+128)/2
            elif img[r, c] >= 128 and img[r, c] < 228:
                img[r, c] = (128+228)/2
            else:
                img[r, c] = (228+255)/2

    cv2.imwrite('panda_threshold.jpg', img)
#############################################################
