import numpy as np

### Define filter arrays to use in conv.py

line_middle_3 = np.array([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
])

line_middle_5 = np.array([
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
])