# Tu tarea es escribir una función que verifique si un número es primo o no.
# La función:
# se llama is_prime;
# toma un argumento (el valor a verificar)
# devuelve True si el argumento es un número primo, y False de lo contrario.


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()