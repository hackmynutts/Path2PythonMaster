# Slicing o Rebanada
#
# Una rebanada es una secuencia de elementos de una lista.
# Los elementos de la rebanada son copiados de la lista original.


# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)


# siempre sera new_list = my_list[inicio:fin-1]
#copiando una porcion de la lista

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#rebanadas con indices negativos

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

#mala practica
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]#fuera de rango
print(new_list)#devolvera una lista vacia

#Rebanada sin inicio

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

#Rebanada sin fin

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)


#eliminar seccion de lista del list[start:end]
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

#vaciar lista
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

#Eliminar la lista de memoria
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list) #dara error de ejecucion


#verificar si un elemento existe en la lista usando in y not in
my_list = [10, 8, 6, 4, 2]
print(8 in my_list)
print(8 not in my_list)