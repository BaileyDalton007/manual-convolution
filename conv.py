import load_image as load
import filters

# Loads image to a numpy array
array = load.img_to_arr("test.jpg")

# Loads filter array
filter = filters.line_middle

# Calculates shape of the output array without zero-padding
new_shape = (array.shape[0] - (filter.shape[0] - 1), array.shape[0] - (filter.shape[0] - 1))
