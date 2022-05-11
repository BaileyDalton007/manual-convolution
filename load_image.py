from PIL import Image, ImageOps
import numpy as np

# Takes a path of an image and returns a 2D numpy array
# rounding_scale is the amount of decimal places the numpy array will store when scaling image from 0-255 to 0-1
def img_to_arr(path, rounding_scale=2):
    # Opens the current test image and grayscales it
    im = Image.open(path)
    gray_image = ImageOps.grayscale(im)

    # Loads the image into a 2 dimensional numpy array
    pix = np.array(gray_image)

    # Scale pixels from 0-255 to 0-1
    pix = np.round_(pix / 255, decimals=rounding_scale)

    return pix

# Convert the modified array to an image object and display it
def show_image_from_arr(arr):
    output = Image.fromarray(np.uint8(arr*255))
    output.show()