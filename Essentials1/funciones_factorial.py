#que es un factorial? producto de todos los números naturales previos al argumento o número dado.
# 0! = 1 (¡Si!, es verdad)
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# :
# :
# n! = 1 * 2 * 3 * 4 * ... * n-1 * n

def factorial (n):
    if n < 0:
        return None
    elif n < 2: #0 y 1 scenario
        return 1
    else:
        producto = 1
        for i in range(2, n + 1):
            producto *= i
        return producto
    


for n in range (1,9):
    print(f"El factorial de {n} es {factorial(n)}")


#recursividad
#Que es recursividad? una funcion que se llama a si misma
#factorial recursivo

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)


for n in range (1,9):
    print(f"El factorial de {n} es {factorial_function(n)}")