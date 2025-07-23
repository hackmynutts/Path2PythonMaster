my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]

largest = my_list[0]

for i in range(1, len(my_list)):#aqui trabajamos con i que es cada uno de los indices
    if my_list[i] > largest:
        largest = my_list[i]

print("El elemento mayor de la lista es:", largest)

#version mejorada
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list: #aca trabajamos con i que es cada uno de los elementos
    if i > largest:
        largest = i
 
print("El elemento mayor de la lista es:",largest)


