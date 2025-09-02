
# Un programa que calcula la altura de una pirámide de bloques.
# la premisa es que cada capa se compone de un bloque mas que la anterior

blocks = int(input("Ingresa el número de bloques: "))

height = 0
required_blocks = 1  # La altura inicial es 1 bloque para tener una base y saber cuantas capas hay

while blocks >= required_blocks:
    blocks -= required_blocks
    height += 1
    required_blocks += 1

print("La altura de la pirámide:", height)
