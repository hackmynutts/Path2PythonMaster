#modulo os 
#nos da acceso a varias funciones relacionadas con el sistema operativo
#se utiliza para crear y eliminar carpetas 
#muy parecido a trabajar con command prompt
import shutil 
import os


#trabajando con raw string 
#perfecto para almacenar urls
path = r"C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/REAL PYTHON BOOK/"


                    # ../es para subir una carpeta                 
shutil.copy((path+"../hello.txt"),(path+"/shutil_folder/hi3.txt")) #aca jugamos con la ubicacion 
                                                                   #el folder con el salto '../' 
                                                                   