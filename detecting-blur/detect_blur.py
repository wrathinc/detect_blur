# USAGE
# python detect_blur.py 

# import the necessary packages
from imutils import paths
import numpy as np 
import argparse
import cv2
import os, time 
import folders

start = time.time()
folders.__folder__.create_folders()

def laplacian(image):
	''' Parameters
		src:	Source image.
		dst:	Destination image of the same size and the same number 
			of channels as src.

		ddepth:	Desired depth of the destination image.
		ksize:	Aperture size used to compute the second-derivative filters.
				See getDerivKernels for details. 
				The size must be positive and odd.
		scale:	Optional scale factor for the computed 
				Laplacian values. By default,
			 no scaling is applied. See getDerivKernels for details.
		delta:	Optional delta value that is added to the results
			 prior to storing them in dst .
		borderType:	Pixel extrapolation method, see BorderTypes
		Python:
		dst	=	cv.Laplacian(	src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]	)
 	'''
	return cv2.Laplacian(image, cv2.CV_64F).var()

def image_process(image):
	''' image_process passes 
		args  : ap.argarse.ArgumentParser()


		usage : 
			ArgumentParser parses arguments 
			through the parse_args() method.
			This will inspect the command line,
			 convert each argument to the appropriate; 
			type and then invoke the appropriate action. 
			In most cases, this means a simple
			Namespace object will be built up from attributes 
			parsed out of the command line:
	'''

	ap = argparse.ArgumentParser()
	ap.add_argument("-t", "--threshold", type=float, default=200.0, 
	help="focus measures that fall below this value will be considered 'blurry'")
	args = vars(ap.parse_args())
	src_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	frequency_varince = laplacian(src_gray)
	dirpath = os.getcwd()
	try:
		if frequency_varince < args["threshold"]:
			cv2.imwrite(dirpath+"/not_blurry/image{}.jpg".format(frequency_varince),image) #--> sorts image into folders based on the vaule of lapcian
		
	except(RuntimeError, TypeError, NameError) as e:
		print(e)

	else:
		if frequency_varince > args["threshold"]:
			cv2.imwrite(dirpath+"/blury_photo/image{}.jpg".format(frequency_varince),image)#--> sorts image into folders based on the vaule of lapcian
	
	   
def imagePath(img):
	''' image path 
	expression: dir
	returns a image.
	'''
	j = cv2.imread(img)
	image_process(j)
	
def main():
	'''main function runs a forloop though our directory images'''
	print("main_loop")
	for file in paths.list_images("images"):
		imagePath(file)





if __name__ == "__main__":
	main()





print(time.time()-start)