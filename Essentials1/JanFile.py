counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

#############################

counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

#############################

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

numero = int(input("¿Cuál es el número secreto? "))

while numero != secret_number:
    print("El número secreto es diferente. Inténtalo de nuevo.")
    numero = int(input("¿Cuál es el número secreto? "))

print("¡Bien hecho, muggle! Eres libre ahora.")


#############################

import time
for i in range(6):
    print(i, "Mississippi")
    time.sleep(1)

print("¡Listo o no, ahí voy!")


