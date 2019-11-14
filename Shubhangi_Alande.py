## ---------------------------- ##
## 
## sample_student.py
##
## Example student submission for programming challenge. A few things: 
## 1. Before submitting, change the name of this file to your firstname_lastname.py.
## 2. Be sure not to change the name of the method below, classify.py
## 3. In this challenge, you are only permitted to import numpy and methods from 
##    the util module in this repository. Note that if you make any changes to your local 
##    util module, these won't be reflected in the util module that is imported by the 
##    auto grading algorithm. 
## 4. Anti-plagarism checks will be run on your submission
##
##
## ---------------------------- ##


import numpy as np

def filter_2d(im_cropped, kernel):
    M = kernel.shape[0]
    N = kernel.shape[1]
    H = im_cropped.shape[0]
    W = im_cropped.shape[1]
    
    filtered_image = np.zeros((H-M+1, W-N+1), dtype = 'float64')

    for i in range(filtered_image.shape[0]):
        for j in range(filtered_image.shape[1]):
            image_patch = im_cropped[i:i+M, j:j+N]
            filtered_image[i, j] = np.sum(np.multiply(image_patch, kernel))

    return filtered_image

def convert_to_grayscale(cropped):
    '''
    Convert color image to grayscale.
    '''
    return np.mean(cropped, axis = 2)

def classify(im):
    '''
    Example submission for coding challenge. 
    Args: im (nxmx3) unsigned 8-bit color image 
    Returns: One of three strings: 'brick', 'ball', or 'cylinder'  
    '''
    im_cropped=im[25:225,25:225]
    gray = convert_to_grayscale(im_cropped/255.)
   # plt.imshow(gray, cmap = 'gray')
    Kx = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]])

    Ky = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]])

    Gx = filter_2d(gray, Kx)
    Gy = filter_2d(gray, Ky)

    #Compute Gradient Magnitude and Direction:
    G_magnitude = np.sqrt(Gx**2+Gy**2)
    G_direction = np.arctan2(Gy, Gx)
    
    edges = G_magnitude > 0.5

    y_coords, x_coords = np.where(edges)
    #print(x_coords)
    
    if len(x_coords) > 0 and len(x_coords) <=865:
        return 'ball'
    elif len(x_coords) >870 and len(x_coords) <=1600:
        return 'cylinder'
    else:
        return 'brick'   
    

     
    