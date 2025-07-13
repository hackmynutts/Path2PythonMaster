#lista es un tipo de variable que puede almacenar mas de un valor en la misma variable
#las listas se definen con corchetes []
#las listas son mutables es decir que si quiere puedo modificar el valor 34 de lista

numbers = [5,7,32,54,77]
print("la lista de numeros es ", numbers)

numbers[0] = 111 #asi asignamos el valor 111 a la posicion 0 de la lista
print("la lista de numeros es con asignacion ", numbers)   

numbers[2] = numbers[4] #asi copia el valor 77 a la posicion 2 de la lista
print("la lista de numeros con copia es ", numbers)

print("\nla longitud de la lista es ", len(numbers)) #asi sabemos la longitud de la lista
print("\nAccediendo al 4to valor  ", numbers[3])# recordar que empieza en 0


###########eliminar de una lista se hace bajo una instruccion del 

numbers = [5,7,32,54,77]
print("la lista de numeros es ", numbers)

del numbers[2] #asi eliminamos el valor 32 de la lista
print(f"la lista de numeros es {numbers} y la longitud es {len(numbers)}") 