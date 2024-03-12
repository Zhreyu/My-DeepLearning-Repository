import cv2
import numpy as np
def apply_hf_filters(image):
    # Note: The exact values of these filters taken from the paper's figure 2.
    kernel1_values = np.array([
    [-1, 2, -1],
    [2, -4, 2],
    [-1, 2, -1]
    ])
    kernel1 = 1/4 * kernel1_values

# Kernel 2
    kernel2_values = np.array([
    [0, -1, 0],
    [-1, 2, -1],
    [0, -1, 0]
])
    kernel2 = 1/2 * kernel2_values

# Kernel 3
    kernel3_values = np.array([
    [-1, 2, -2, 2, -1],
    [2, -6, 8, -6, 2],
    [-2, 8, -12, 8, -2],
    [2, -6, 8, -6, 2],
    [-1, 2, -2, 2, -1]
])
    kernel3 = 1/12 * kernel3_values


    filtered1 = cv2.filter2D(image, -1, kernel1)
    filtered2 = cv2.filter2D(image, -1, kernel2)
    filtered3 = cv2.filter2D(image, -1, kernel3)
    
    # avg of three filters, need to be adjusted
    hf_image = (filtered1 + filtered2 + filtered3) / 3.0
    return hf_image

def apply_lf_filters(image):
    # The gaussianblur radaii in paper are (4,6,9) but it throws error ,
    #  we can go with sigma values 4,6,9
    blur1 = cv2.GaussianBlur(image, (3, 3), 0)
    blur2 = cv2.GaussianBlur(image, (5, 5), 0)
    blur3 = cv2.GaussianBlur(image, (7, 7), 0)
    
    #adjust as needed
    lf_image = (blur1 + blur2 + blur3) / 3.0
    return lf_image