# USAGE
# python detect_blur.py 
from imutils import paths
import numpy as np 
import argparse  as give_argument
import cv2
import os, time 
from folders import __folder__
from blur_filter import blur_laplacian

start = time.time()

__folder__.create_folders(self=__file__)

def image_process(image):
	''' image_process 
		args	    :   images
		function    :   cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
						blur_laplacian.laplacian(src_gray)
		usage 		: 
						coverts the image into gray
						returns vaule for function bulr_laplacian
	'''
	src_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)	
	frequency_varince = blur_laplacian.laplacian(src_gray)
	imageSort(frequency_varince,image)


def imageSort(frequency_varince,image):
	""" have a dict for now that sets a threshold vaule for how
		sort the image. Then we use cv2.imwrite to save the image in a folder.

		args	: freqency_varince, image
		usage : sort images into folders 

	 """
	args = {"threshold":200}

	try:
		if frequency_varince < args["threshold"]:
			cv2.imwrite(os.getcwd()+"/not_blurry/image{}.jpg".format(frequency_varince),image) #--> sorts image into folders based on the vaule of lapcian
		
	except(RuntimeError, TypeError, NameError) as e:
		print(e)

	else:
		if frequency_varince > args["threshold"]:
			cv2.imwrite(os.getcwd()+"/blury_photo/image{}.jpg".format(frequency_varince),image)#--> sorts image into folders based on the vaule of lapcian
	


def main():
	'''main function runs a forloop though our directory images'''

	for file in paths.list_images("images"):
		image = cv2.imread(file)
		image_process(image)
		


if __name__ == "__main__":
	main()

print(time.time()-start)