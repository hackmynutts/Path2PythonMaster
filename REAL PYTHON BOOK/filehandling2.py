#modulo os 
#nos da acceso a varias funciones relacionadas con el sistema operativo
#se utiliza para crear y eliminar carpetas 
#muy parecido a trabajar con command prompt
import shutil 
import os


#trabajando con raw string 
#perfecto para almacenar urls
path = r"C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/REAL PYTHON BOOK/"

#eliminar un archivo
#syntax os.remove(path)

os.remove(path+"shutil_folder/hi3.txt")
                    # ../es para subir una carpeta                 
shutil.copy((path+"../hello.txt"),(path+"/shutil_folder/hi4.txt")) #aca jugamos con la ubicacion 
                                                                   #el folder con el salto '../' 
                                                                   

#Utilizar os para crear carpetas
#syntax os.mkdir(path)
os.mkdir(path+"test_folder1")

#Utilizar os para eliminar carpetas
#syntax os.rmdir(path)
#cabe recalcar que solo eliminara carpetas vacias!!! 
os.rmdir(path+"test_folder")