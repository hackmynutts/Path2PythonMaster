# la idea es que eliminemos los valores repetidos de la lista
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
indices = []

for i in range(len(my_list)): #necesitamos (10 - 1) comparaciones
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
            if j not in indices:  # ← evitar duplicados en 'indices'
                indices.append(j)

indices.sort(reverse=True)  # ordenar del mayor al menor

for index in indices:
    del my_list[index]

print("La lista con elementos únicos:")
print(my_list)

# Cuando eliminas elementos por índice, hazlo de mayor a menor.
# No modifiques la lista de índices dentro del bucle.
# Asegúrate de que indices no contenga duplicados 
# (usa if j not in indices o un set).
# Evita cálculos innecesarios como index - i a menos 
# que entiendas bien cómo se afecta el índice por cada eliminación.