
# La instrucción break se implementa para salir/terminar un bucle.

# Diseña un programa que use un bucle while y le pida continuamente al usuario 
# que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de output secreta, 
# en cuyo caso el mensaje "Has dejado el bucle con éxito." 
# debe imprimirse en la pantalla y el bucle debe terminar.
# No imprimas ninguna de las palabras ingresadas por el usuario. 
# Utiliza el concepto de ejecución condicional y la sentencia break.


palabra = input("Ingrese una palabra")
while (palabra!="chupacabra") :
    palabra = input("Ingrese una nueva palabra")

print("Has dejado el bucle con éxito.")