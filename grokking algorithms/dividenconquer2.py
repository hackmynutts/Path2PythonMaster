# suma de los items de  una lista de manera recursiva
numb = [2,3,4,5,6,9,34,99]

def sumArray(arreglo):
    if len(arreglo) == 0:
        return 0
    else:
        return arreglo[0] + sumArray(arreglo[1:])

print(f"la suma del los valores del arreglo son: {sumArray(numb)}")

# count items in a list


def maxIteminArray(arreglo):
    mayor = arreglo[0]
    if len(arreglo) == 1:#debe ser 1 porque no queremos trabajar con una lista vacia...
        return mayor
    elif(mayor<arreglo[0]):
        mayor=arreglo[0]
        return maxIteminArray(arreglo[1:])
    else:
        return maxIteminArray(arreglo[1:])

print(f"el numero mayor del arreglo es: {maxIteminArray(numb)}")



def countItemsArray(arreglo):
    if len(arreglo) == 0:
            return 0
    else:
         return 1 + countItemsArray(arreglo[1:])

print(f"la cantidad de items en el arreglo son: {countItemsArray(numb)}")