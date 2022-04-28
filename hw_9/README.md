# Python AY 250 Homework

Homework submissions for AY 250, Spring 2022.
Name: STEVEN LEE

## Homework 9
[Homework 9](https://github.com/stevensslee/python-ay250-homeworks/blob/main/hw_9/hw_9.ipynb) was completed on Apr. 27, 2022.


Asteroid Tracking:
I could not improve upon the asteroid_solution.ipynb notebook in the asteroid folder. 

Panorama Stitching:
Three overlapping images of cows are used in adv3_panorama-stitching-solution.ipynb(the images are titled PXL_2021081*). The images were downsampled by a factor of 10 in x and y from 3024,4032 pixels to 303,404 pixels to speed up the ORB algorithm. The resulting cows can be seen in the cows_nolines.jpg and connected_black_and_white_cows.png. The colored reconstruction at the bottom of the notebook did not work.

Image Stacking:

Image stacking was performed by following the steps outlined at https://learn.astropy.org/tutorials/FITS-images.html with the Cas A data from https://chandra.harvard.edu/photo/openFITS/. Directions available here https://chandra.harvard.edu/photo/openFITS/casa.html for gimp image stacking were adapted to python and scikit-image. I only smoothed the images using the median filter and did not do any of the nonlinear transformations on the layers(there was only 1 layer in my data). The resulting images are saved as casa_filtered or casa_unfiltered where the filtered images have the applied median filter. The casa_filtered_final.jpg and casa_unfiltered_final.jpg correspond to the stacked image, while the casa_filtered.jpg and casa_unfiltered.jpg show from left to right the soft, medium, hard x-ray images and the stacked image. The images are all in log scale except for casa_filtered_normalscale.jpg. 
