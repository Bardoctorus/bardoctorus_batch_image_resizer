from __future__ import print_function
from PIL import Image
import os, sys




im = Image.open("/home/ian/Downloads/me_stage_1.jpg")
imPath = "/home/ian/Downloads/me_stage_1.jpg"
baseName = os.path.basename(imPath)
strippedName = os.path.splitext(baseName)[0]
#print(strippedName)
newWidth = 670




#print(im.format,im.size, im.mode)


def resizer(im, newWidth):

	newHeight = int(newWidth * im.size[1] / im.size [0])
	newSize = (newWidth, newHeight)

	newIm = im.resize(newSize, Image.LANCZOS)
	newFilename = (strippedName + "_670.jpg")
	print("saved as: "+newFilename)
	newIm.save(newFilename, "JPEG")
	#print()

#print(im.size)

#print(newSize)
resizer(im,newWidth)