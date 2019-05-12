from PIL import Image
import os, sys, glob

from os import listdir
from os.path import isfile, join


#  main should check everything is ok then do stuff
def main(folder, newWidth):
    print(folder, type(folder))
    
    if newWidth != type(int):
        try:            
            newWidth = int(newWidth)
           
            print(newWidth, type(newWidth))
        except:
            print("New width must be an integer, exiting")
            sys.exit(1)
      
    if not os.path.exists(folder):
        print("The folder isn't valid, exiting")
        sys.exit(1)

    

    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    print(onlyfiles)

    for file in onlyfiles:
        file_checker(file,newWidth)


def file_checker(file, newWidth):
    try:
        f = Image.open(file)
        if (f.size > newWidth):
            makeBigga(f)
        elif (f.size < newWidth):
            makeSmol(f)
        else:
            print("Image already correct width - moving on")
            return
    except:
        print("Couldn't open file: "+file+" - moving on")    
        return
    


def makeBigga(file):
    print("this is big time")

def makeSmol(file):
    print("squashy squashy")    

def saveTing():
    print("super saver")
    
if __name__ == "__main__":
    path = input("Enter folder path, or leave blank to use current folder.\n.")
    if path == "":
        path = os.getcwd()
    size = input("Enter new width.\n.") 
    main(path, size)