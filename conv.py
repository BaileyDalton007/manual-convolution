import load_image as load
import filters
import numpy as np

# Loads image to a numpy array
array = load.img_to_arr("test.jpg")

# Loads filter array
filter = filters.line_middle_5

# Calculates shape of the output array without zero-padding
new_shape = (array.shape[0] - (filter.shape[0] - 1), array.shape[0] - (filter.shape[0] - 1))

# Iterating through input image taking the dot product of the input and kernel
output_array = []
for row in range(new_shape[0]):
    output_row = []

    for column in range(new_shape[1]):
        # Defines current kernel matrix
        kernel = np.array([array[row:row + filter.shape[1], column:column + filter.shape[0]]])
        #kernel = np.array([array[:filter.shape[1], :filter.shape[0]]])

        output = np.sum(np.dot(filter, kernel))
        output_row.append(output)
    
    output_array.append(output_row)

output = np.array(output_array)

rel_max = np.amax(output)
output = np.round_(output / rel_max, decimals=3)

load.show_image_from_arr(output)