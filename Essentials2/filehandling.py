#manejo de archivos raw 
#funcion open
#open(filename, mode)
#modes
#r -> read
#r+ -> read and write
#w -> write
#w+ -> read and write
#a -> append

myOutput = open("hello.txt", "w")
myOutput.write("DONE by Jorge!\n")
myOutput.writelines("Hello, world!\nThis is my first file written with Python.")
myOutput.close()


#append
myOutput = open("hello.txt", "a")
myOutput.write("\nThis is a new line added by append.")
myOutput.close()

#leer
myInput = open("hello.txt", "r")
print(myInput.read()) #este devuelve una cadena de string completa
print (myInput.readlines()) #este devuelve una lista de las cadenas
myOutput.close()

#imprimir asi genera que el ultimo readlines devuelva una lista vacia
#esto es debido a que el cursor se encuentra al final del archivo
#esto lo podemos solucionar con seek
#seek(offset, origin)

myInput = open("hello.txt", "r")
print(myInput.read()) 
myInput.seek(0)
print (myInput.readlines()) 
myOutput.close()


#leer mediante un bucle for

myInput = open("hello.txt", "r")
for line in myInput:
    print(line)
myInput.close()


#leer mediante un bucle while

myInput = open("hello.txt", "r")
print("leer mediante un bucle while")
while True:
    line = myInput.readline()
    if not line:
        break
    print(line)
myInput.close()


#implementando el with
with open("hello.txt", "r") as myInput:
    for line in myInput:
        print(line),


#leer y escribir
with open("hello.txt", "r") as myInput, open("hi.txt", "w") as myOutput:
        for line in myInput:
            myOutput.write(line)