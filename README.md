# Manual Convolution
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BaileyDalton007/manual-convolution)

## Usage
TODO

## Overview
### load_image.py
This file loads an image, grayscales it, scales it from values from 0-255 for each pixel to 0-1 for each pixel. 

```ROUNDING_SCALE``` is a constant that can be set in ```load_image.py```. It determines the amount of decimal places in the float of each pixel being scaled down from 255. Here is what the image looks like with a ```ROUNDING_SCALE``` of 0:

![image](https://user-images.githubusercontent.com/59097689/167962306-125aa359-3fbe-4e4c-a6e5-19ec16e57f08.png)

And here is what the same image looks like with a ```ROUNDING SCALE``` of 10:

![image](https://user-images.githubusercontent.com/59097689/167962463-0cdf8bdb-9a46-405b-8bea-2f6f8c42b490.png)


With 0 decimal places, each pixel is either 0 or 1 (black or white), while the image with 10 decimal places conserves the variety of gray tones in the orginal image.
