# Manual Convolution
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BaileyDalton007/manual-convolution)

## Usage
TODO

## Overview
### load_image.py
This file loads an image, grayscales it, scales it from values from 0-255 for each pixel to 0-1 for each pixel. 

```rounding_scale``` is a parameter for ```img_to_array()```. It determines the amount of decimal places in the float of each pixel being scaled down from 255. Here is what the image looks like with a ```rounding_scale``` of 0:

![image](https://user-images.githubusercontent.com/59097689/167962306-125aa359-3fbe-4e4c-a6e5-19ec16e57f08.png)

And here is what the same image looks like with a ```rounding_scale``` of 10:

![image](https://user-images.githubusercontent.com/59097689/167962463-0cdf8bdb-9a46-405b-8bea-2f6f8c42b490.png)


With 0 decimal places, each pixel is either 0 or 1 (black or white), while the image with 10 decimal places conserves the variety of gray tones in the orginal image.

### filters.py
This file defines the filter matricies used in ```conv.py```. Just define a 2D numpy array and then refrence it as the filter in ```conv.py```

### conv.py
```conv.py``` is the main file, the file that will be run to handle the convolution operation. It iterates through each pixel of the shape of the new output matrix and applies dot product summation to each. Afterwards it converts the output to a numpy array and then to an image.