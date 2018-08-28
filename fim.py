from __future__ import print_function
from PIL import Image
import os, sys
import glob

def confirm():
	print("This will create a new directory at: "+newFol) 
	print("(That is, if it doesn't already exist.)")
	print("Images resized to "+sys.argv[2]+"px width will be placed there.") 
	print("Continue? yes/no")
	choice = input().lower()
	if choice in y:
		return True
	elif choice in n:
		sys.exit("Operation cancelled")
	else:
		sys.stdout.write("Please respond with 'yes' or 'no'")

#input string variables
y = {'yes', 'y', 'ye'}
n = {'no', 'n'}


dirPath = sys.argv[1]
newWidth = int(sys.argv[2])

newFol = sys.argv[1]+"\\"+"batch_resized_images"

keepOn = confirm()



if keepOn and not os.path.exists(newFol):
	
	os.makedirs(newFol)
	
	print("\n Successfully created: "+newFol+"\n\n")



"""
baseName = os.path.basename(imPath)
strippedName = os.path.splitext(baseName)[0]
#print(strippedName)
newWidth = int(sys.argv[2])
"""




#print(im.format,im.size, im.mode)



def resizer(im, newWidth, origName):

	print("Opening:")
	print(origName +"\n")

	newHeight = int(newWidth * im.size[1] / im.size [0])
	newSize = (newWidth, newHeight)

	newIm = im.resize(newSize, Image.LANCZOS)

	newBase = os.path.basename(origName)
	newName = os.path.splitext(newBase)[0]
	

	#newFilename = (sys.argv[1] + "_resizedto"+sys.argv[2]+".jpg")
	print("Saved as:")
	print(newFol+ "\\" +newName+"_"+sys.argv[2]+".jpg"+"\n")
	newPath = newFol+ "\\" +newName+"_"+sys.argv[2]+".jpg"
	newIm.save(newPath, "PNG")
	

#print(im.size)

#print(newSize)

for img in glob.glob(sys.argv[1]+"\\*.jpg"):
	
	try:
		changeIm = Image.open(img)
		resizer(changeIm,newWidth , img)
	except IOError:
		print("cannot resize ", img)

for img in glob.glob(sys.argv[1]+"\\*.png"):

	try:
		changeIm = Image.open(img)
		resizer(changeIm,newWidth , img)
	except IOError:
		print("cannot resize ", img)

for img in glob.glob(sys.argv[1]+"\\"+sys.argv[3]):
	
	print(img)
	try:
		changeIm = Image.open(img)
		resizer(changeIm,newWidth , img)
	except IOError:
		print("cannot resize ", img)
#resizer(im,newWidth)