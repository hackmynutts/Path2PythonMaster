#programa para renombrar archivos
import os

path = "C:/Users/jorge/OneDrive/Escritorio/wallpaper"

fileNameList = os.listdir(path)#me da la lista de los nombres de cada archivo

for fileName in fileNameList:
    if not fileName.endswith(".jpg") or fileName.endswith(".png"): ##.endswith verifica que el archivo termine con .jpg o .png respectivamente
        print(f"Changing to {fileName} to jpg")        
        fullFileName = os.path.join(path, fileName) 
        newFileName = fullFileName[0:len(fullFileName)-4] + ".jpg" 
        os.rename(fullFileName, newFileName) #renombrar el archivo


#buscando folder dentro de folder
#con glob
import glob

path = "C:/Users/jorge/OneDrive/Escritorio/"

possibleFiles = os.path.join(path, "*/*.jpg")#con esto buscamos dentro de cualquier carpeta
                                             #y dentro de cualquier subcarpeta

for fileName in glob.glob(possibleFiles):
    print(fileName)



#recorriendo carpetas con os.walk

path = "C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster"
for currentFolder, subfolders, filenames in os.walk(path):
    print(f"Current folder: {currentFolder}")
    for subfolder in subfolders:
        print(f"Subfolder of {currentFolder}: {subfolder}")
    for filename in filenames:
        print(f"File in {currentFolder}: {filename}")