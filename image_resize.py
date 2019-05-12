from PIL import Image
import os, sys

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

    




def makeBigga():
    print("this is big time")

def makeSmol():
    print("squashy squashy")    

def saveTing():
    print("super saver")
    
if __name__ == "__main__":
    path = input("Enter folder path, or leave blank to use current folder.\n.")
    if path == "":
        path = os.getcwd()
    size = input("Enter new width.\n.") 
    main(path, size)