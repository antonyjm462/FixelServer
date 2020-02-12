import base64
import json
import os

#This conversion is tested for jpg as well as png images

def convimg(image):
	#this converts input image to base64 and stores it in img_data
	with open(image, "rb") as image_file:
	    img_data = base64.b64encode(image_file.read())
	return img_data;


def conv64(img_data,img_type):	
	if "png" in img_type:	
		#the base64 string in img_data is converted to image
		with open("final.png", "wb") as fh:
	   		fh.write(base64.decodebytes(img_data))
	elif "jpg" in img_type:
		#the base64 string in img_data is converted to image
		with open("final.jpg", "wb") as fh:
	   		fh.write(base64.decodebytes(img_data))
def main():
	conv()

if __name__ == '__main__':
    main()
