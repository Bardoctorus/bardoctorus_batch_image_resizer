from __future__ import print_function
from PIL import Image
import os, sys
import glob


#replace all the sys.argv with argparse, use it to show the user how to
#use the thing and also get round missing arguments


def confirm():
	print("\n\nThis will create a new directory at: "+newFol) 
	print("(That is, if it doesn't already exist.)\n")
	print("Images resized to "+newWidth+"px width will be placed there. Aspect Ratio is preserved.") 
	print("Are you SURE you want to continue?\n Yes/No")
	choice = input().lower()
	if choice in y:
		return True
	elif choice in n:
		sys.exit("Operation cancelled")
	else:
		sys.stdout.write("Please respond with 'yes' or 'no'")


def resizer(im, newWidth, origName):

	print("Opening:")
	print(origName +"\n")

	newHeight = int(int(newWidth) * im.size[1] / im.size [0])
	newSize = (int(newWidth), newHeight)

	newIm = im.resize(newSize, Image.LANCZOS)

	newBase = os.path.basename(origName)
	newName = os.path.splitext(newBase)[0]
	


	
	newPath = newFol+ "\\" +newName+"_"+newWidth+".jpg"
	if not os.path.exists(newPath):
		print("Saved as:")
		print(newFol+ "\\" +newName+"_"+newWidth+".jpg"+"\n")
		newIm.save(newPath, "PNG")
	else:
		print("File already exists, moving on.")



#input string variables
y = {'yes', 'y', 'ye'}
n = {'no', 'n'}


dirPath = sys.argv[1]  #  python fim.py PATHTODIR 670
newWidth = sys.argv[2]
newFol = dirPath+"\\"+"batch_resized_images"
keepOn = confirm()
# keepon is pointless i think


if keepOn and not os.path.exists(newFol):
	
	os.makedirs(newFol)
	
	print("\n Successfully created: "+newFol+"\n\n")
else:
	print("Directory already exists, will use it")




for img in glob.glob(dirPath+"\\*.jpg"):
	
	try:
		changeIm = Image.open(img)
		resizer(changeIm,newWidth , img)
	except IOError:
		print("cannot resize ", img)

for img in glob.glob(dirPath+"\\*.png"):

	try:
		changeIm = Image.open(img)
		resizer(changeIm,newWidth , img)
	except IOError:
		print("cannot resize ", img)




""" This doesn't work but argparser will make it work

if sys.argv[3]:
	for img in glob.glob(dirPath+"\\*."+sys.argv[3]):
	
		print(img)
		try:
			changeIm = Image.open(img)
			resizer(changeIm,newWidth , img)
		except IOError:
			print("cannot resize ", img)

"""
