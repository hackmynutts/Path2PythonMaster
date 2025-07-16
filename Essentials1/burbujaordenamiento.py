my_list = [8, 10, 6, 2, 4]  # lista a ordenar
#Es length - 1 porque ya comparamos el primer elemento con el segundo
for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.
        print("Intercambio: ", my_list)

print("Lista ordenada: ", my_list)


######### FORMA CORRECTA DE ORDENAMIENTO BURBUJA#############
my_list = [8, 10, 6, 2, 4]

n = len(my_list)
print("Lista desordenada:", my_list)
for i in range(n):  # n pasadas
    for j in range(n - 1 - i):  # se reduce en cada iteración
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            print(f"Intercambio en paso {i+1}, índice {j}: {my_list}")

print("Lista ordenada:", my_list)


##############OTRA FORMA DE RESOLVER EL PROBLEMA####################
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

