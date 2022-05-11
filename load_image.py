from PIL import Image, ImageOps

import numpy as np

import matplotlib
import matplotlib.pyplot as plt

# The amount of decimal places the numpy array will store when scaling image from 0-255 to 0-1
ROUNDING_SCALE = 0

# Opens the current test image and grayscales it
im = Image.open(r"test.jpg")
gray_image = ImageOps.grayscale(im)

# Loads the image into a 2 dimensional numpy array
pix = np.array(im)

# Scale pixels from 0-255 to 0-1 
pix = np.round_(pix / 255, decimals=ROUNDING_SCALE)

output = Image.fromarray(np.uint8(pix*255))

output.show()