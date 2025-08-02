# This is a GIF generator which create a GIF from images 

import imageio.v3 as iio

# filesnames contain the list of the location of images
filesnames = ["image3.png", "image1.png"]

# images is empty list that store the actual image from these files
images = [ ]

# for loop is used to go through file paths and read the images using imageio library 
for filename in filesnames:
    print(f"Loading {filename}") 
    images.append(iio.imread(filename))

# imwrite method is to turn the image into GIF
iio.imwrite("final.gif" , images , duration = 550 , loop = 0) 

# duration is in millisecond;loop = 0 means the GIF loops forever 

