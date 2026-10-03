from os import listdir
from os.path import join, isfile

def printnames(searchfolder):
    for file in sorted(listdir(searchfolder)):#loop through ever file and folder
        fullpath = join(searchfolder,file)
        if isfile(fullpath):
            print(file)
        else:
            printnames(fullpath) #recurse to keep looking
printnames("C:/Users/jorge/OneDrive/Pictures")
