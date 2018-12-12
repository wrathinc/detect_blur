# USAGE
# python detect_blur.py 
from imutils import paths
import numpy as np 
import argparse
import cv2
import os, time 
from folders import __folder__
from blur_filter import blur_laplacian

start = time.time()

__folder__.create_folders(self=__file__)

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
	blur_laplacian.laplacian(self=image)
	ap = argparse.ArgumentParser()
	ap.add_argument("-t", "--threshold", type=float, default=200.0, 
	help="focus measures that fall below this value will be considered 'blurry'")
	args = vars(ap.parse_args())
	src_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	frequency_varince = blur_laplacian.laplacian(src_gray)
	dirpath = os.getcwd()
	try:
		if frequency_varince < args["threshold"]:
			cv2.imwrite(dirpath+"/not_blurry/image{}.jpg".format(frequency_varince),image) #--> sorts image into folders based on the vaule of lapcian
		
	except(RuntimeError, TypeError, NameError) as e:
		print(e)

	else:
		if frequency_varince > args["threshold"]:
			cv2.imwrite(dirpath+"/blury_photo/image{}.jpg".format(frequency_varince),image)#--> sorts image into folders based on the vaule of lapcian
	
	   
def main():
	'''main function runs a forloop though our directory images'''
	for file in paths.list_images("images"):
		image = cv2.imread(file)
		image_process(image)


if __name__ == "__main__":
	main()

print(time.time()-start)