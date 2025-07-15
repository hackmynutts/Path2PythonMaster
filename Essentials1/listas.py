# #lista es un tipo de variable que puede almacenar mas de un valor en la misma variable
# #las listas se definen con corchetes []
# #las listas son mutables es decir que si quiere puedo modificar el valor 34 de lista

# numbers = [5,7,32,54,77]
# print("la lista de numeros es ", numbers)

# numbers[0] = 111 #asi asignamos el valor 111 a la posicion 0 de la lista
# print("la lista de numeros es con asignacion ", numbers)   

# numbers[2] = numbers[4] #asi copia el valor 77 a la posicion 2 de la lista
# print("la lista de numeros con copia es ", numbers)

# print("\nla longitud de la lista es ", len(numbers)) #asi sabemos la longitud de la lista
# print("\nAccediendo al 4to valor  ", numbers[3])# recordar que empieza en 0


# ###########eliminar de una lista se hace bajo una instruccion del 

# numbers = [5,7,32,54,77]
# print("la lista de numeros es ", numbers)

# del numbers[2] #asi eliminamos el valor 32 de la lista
# print(f"la lista de numeros es {numbers} y la longitud es {len(numbers)}") 


# ############# agregar elementos a una lista

# numbers = [5,7,32,54,77]
# print("la lista de numeros es ", numbers)

# numbers.append(111) #asi agregamos el valor 111 a la lista
# print(f"la lista de numeros es {numbers} y la longitud es {len(numbers)}")

# #tambien podemos decidir en que posicion agregar un elemento

# #list.insert(posicion,elemento)

# numbers = [5,7,32,54,77]
# print("la lista de numeros es ", numbers)

# numbers.insert(2,111) #asi agregamos el valor 111 en la posicion 2 de la lista
# print(f"la lista de numeros es {numbers} y la longitud es {len(numbers)}")

# #######podemos tambien crear la lista vacia e ir agregando elementos como necesitemos

# list = []

# for i in range(5):
#     list.append(i)#NOTA: si lo dejamos sin i+1 el resultado seria 0,1,2,3,4 ya que empezamos desde 0
#     print(f"la lista de numeros es {list} y la longitud es {len(list)}")

# print(list)

# ########## uso de listas
# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):#usamos la longitud de nuestra lista como factor de salida
#     total += my_list[i]

# print(total)#27

#otro approach

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list: #el proceso se repite tantas veces como elementos tenga la lista
    total += i #i tomara el valor de cada una de las posiciones de la lista
print(total)#27