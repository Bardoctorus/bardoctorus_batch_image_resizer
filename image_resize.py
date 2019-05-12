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
    #print(type(onlyfiles[0]))
    succesful_conversions = []
    for file in onlyfiles:
        joined_name = os.path.join(folder, file)
        print("Attempting to open "+joined_name)
        try:
            f =  Image.open(joined_name)

        except IOError:
            print("Error opening "+file+", moving on")
            continue
        else:
            
            newHeight =  int(newWidth * f.size[1]/f.size[0])
            newSize = (newWidth, newHeight)
            newFileName = os.path.join(folder,  "_"+str(newWidth)+"px_"+file)
            # deets = {"new height": newHeight,
            #      "new Size": newSize,
            #      "new file name": newFileName  }
            # print(deets)  
            g = resizer(f, newSize)
            g.save(newFileName)
            succesful_conversions.append(newFileName)
            #print("Created: "+newFileName)
    print(".\n.\n.\n.\nDone! Created:\n")
    for thing in succesful_conversions:
        print (thing)

    
    
def resizer(imData, newSize):
    # ! all this if logic is only needed if you are using a different filter for up/downscaling
      # if (f.size[0] > newSize[0]):
          
        #     g = makeSmol(f, newSize)
            
        #     g.save(newName)
        # elif (f.size[0] < newWidth):
        #     g = makeBigga(f, newSize)
            
        #     g.save(newName)
        # else:
        #     print("Image already correct width - moving on")
        #     return
    g = imData.resize((newSize),Image.LANCZOS)
    return g


    
if __name__ == "__main__":
    print(".______   .______    __  .______     ") 
    print("|   _  \  |   _  \  |  | |   _  \     ")
    print("|  |_)  | |  |_)  | |  | |  |_)  |    ")
    print("|   _  <  |   _  <  |  | |      /     ")
    print("|  |_)  | |  |_)  | |  | |  |\  \-.")
    print("|______/  |______/  |__| | _| `.__| Bardoctorus Batch Image Resizer\n")
    print("This simple image resizer detects all the images in a folder and resizes them to a chosen pixel width using Lanczos, while preserving the aspect ratio.")
    print("\n\nNo files are overwritten, new files get the prefix '_NEWSIZEpx_'")
    
    print("Press Ctrl + C to quit\n\n")
    path = input("Enter folder path, or press Enter to use current folder, or info for more info\n.")
    if path == "":
        path = os.getcwd()
    elif path == "info":
        print("\nFull info available at https://github.com/Bardoctorus/UPDATETHISURL but in short:\n")
        print("This script iterates over every file in a directory using Pillow's Image.open function.")
        print("I'm pretty much just letting it do its thing in a try, and excepting any IOErrors before continuing.")
        print("New file aspect ratios are just 'new_width * old_height / old_width' casted to an int which I'm sure makes some of you cry.")
        print("Feel free to fork and improve this program and tell me how much I suck - @ianmbuckley on the twitderp\n\n")
        path = input("Enter folder path, or press Enter to use current folder.\n.")
        if path == "":
            path = os.getcwd()
    size = input("Enter new width.\n.") 
    main(path, size)



                                      