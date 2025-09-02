#hablaremos sobre el modulo shutil
#el modulo shutil se utiliza para copiar archivos y directorios
import shutil

#copiar un archivo
#syntax shutil.copyfile(source, destination)
shutil.copyfile("C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/hello.txt",
                 "C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/hi.txt")

#syntax shutil.copy(source, destination)
shutil.copy("C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/hello.txt",
                 "C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/REAL PYTHON BOOK/shutil_folder/hi2.txt")
                                                                                        #sino existe el archivo lo crea

#mover / renombrar un archivo
#syntax shutil.move(source, destination)
shutil.move("C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/hi.txt",
                 "C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/REAL PYTHON BOOK/shutil_folder/hi.txt") #cuando decimos renombrar es que el 
                                                                                                                  #destino es el mismo archivo                  
                                                                                                                  #pero con un nuevo nombre



