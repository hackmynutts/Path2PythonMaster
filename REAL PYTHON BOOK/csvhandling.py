# #manejo de archivos csv
# import csv,os,shutil #csv es para manejar archivos csv
# ruta = r"C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/REAL PYTHON BOOK/"
# nombre = input("Indique el nombre del archivo csv que quiere crear:\n")
# myOutput = open(ruta +nombre+".csv", "w")

# file_location = ruta +nombre+ ".csv"
# newName = input("Indique el nombre del archivo csv que quiere renombrar:\n\n")
# wantedName = ruta + newName+".csv"

# myOutput.close()#cerrar el archivo antes de renombrarlo
# #importante porque sino el archivo generara error de que esta abierto

# if os.path.exists(file_location):
#     os.replace(file_location, wantedName) #esto no retorna la ruta simplemente cambia el nombre
#                                       #la ruta seguira almacenada en la variable destino


# #rb es para read binary  
# with open(wantedName, "r") as myInput: #como tenemos Python 3 solo usamos r         
#                                           #pero el nuevo formato es r only
#     shutil.copy(ruta+"wonka.csv", wantedName)
#     myFileReader = csv.reader(myInput) 
#     for line in myFileReader:
#         print(line)

# #unpack un csv 
# import csv,os,shutil #csv es para manejar archivos csv
# ruta = r"C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/REAL PYTHON BOOK/"
# nombre = input("Indique el nombre del archivo csv que quiere crear:\n")
# myOutput = open(ruta +nombre+".csv", "w")

# file_location = ruta +nombre+ ".csv"
# newName = input("Indique el nombre del archivo csv que quiere renombrar:\n\n")
# wantedName = ruta + newName+".csv"

# myOutput.close()#cerrar el archivo antes de renombrarlo
# #importante porque sino el archivo generara error de que esta abierto

# if os.path.exists(file_location):
#     os.replace(file_location, wantedName) #esto no retorna la ruta simplemente cambia el nombre
#                                       #la ruta seguira almacenada en la variable destino


# #rb es para read binary  
# with open(wantedName, "r") as myInput: #como tenemos Python 3 solo usamos r         
#                                           #pero el nuevo formato es r only
#     shutil.copy(ruta+"wonka.csv", wantedName)
#     myFileReader = csv.reader(myInput)

#     next(myFileReader) 
#     for Name, lastName, reward in myFileReader:
#         print(f"{Name} {lastName} got: {reward}")

# ##########csv con tabs##########
# import csv,os,shutil #csv es para manejar archivos csv

# ruta = r"C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/REAL PYTHON BOOK/"
# nombre = input("Indique el nombre del archivo csv que quiere crear:\n")
# myOutput = open(ruta +nombre+".csv", "w")

# file_location = ruta +nombre+ ".csv"
# newName = input("Indique el nombre del archivo csv que quiere renombrar:\n\n")
# wantedName = ruta + newName+".csv"

# myOutput.close()#cerrar el archivo antes de renombrarlo
# #importante porque sino el archivo generara error de que esta abierto

# if os.path.exists(file_location):
#     os.replace(file_location, wantedName) #esto no retorna la ruta simplemente cambia el nombre
#                                       #la ruta seguira almacenada en la variable destino


# #rb es para read binary  
# with open(wantedName, "r") as myInput: #como tenemos Python 3 solo usamos r         
#                                           #pero el nuevo formato es r only
#     shutil.copy(ruta+"tabbed wonka.csv", wantedName)
#     myFileReader = csv.reader(myInput, delimiter="\t") #aqui cambiamos el delimitador
#     for line in myFileReader:
#         print(line)



# #escribir a archivos csv
import csv,os,shutil #csv es para manejar archivos csv

ruta = r"C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/REAL PYTHON BOOK/csv files/"
nombre = input("Indique el nombre del archivo csv que quiere crear:\n")
with open(ruta +nombre+".csv", "w") as myOutput:
    myOutputWriter = csv.writer(myOutput)
    myOutputWriter.writerow(["Movie", "Rating"])
    myOutputWriter.writerow(["Interstellar", "9.5"])
    myOutputWriter.writerow(["Se7en", "9.0"])
    myOutputWriter.writerow(["Dark Knight", "9.5"])
    myOutputWriter.writerow(["The Inglorious Basterds", "9.5"])

myRatings = [["Sinners", "7.6"],
             ["Thhe Brutalist", "9.0"],
             ["Pulp Fiction", "8.9"],
             ["The Irishman", "9.7"]]

with open(ruta +"movies.csv", "a") as myOutput:
    myOutputWriter = csv.writer(myOutput)
    myOutputWriter.writerows(myRatings)

