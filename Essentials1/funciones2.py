#palabra reservada return
def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return

    print("¡Feliz año nuevo!")

happy_new_year() #si imprime el feliz año nuevo
happy_new_year(False) #no imprime el feliz año nuevo

#return con expresion
#def function():
#    return expression

def boring_function():
    return 123

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)

#tambien se permite inutilizar el return

def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123 #no se usa pese a que devuelve un valor

print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")


#primeros vistas del valor none
def saludar(nombre):
    if not nombre:
        return  # Sale de la función sin devolver nada
    print(f"Hola, {nombre}!")

resultado = saludar("")  
print(resultado)  # Muestra: None

#pero que es un none?
def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1)) #muestra none porque la funcion no contempla ese escenario

#listas y funciones
#enviando lista como argumento
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([1, 2, 3, 4, 5]))
#que no hacer
print(list_sum(5))# TypeError: 'int' object is not iterable

#retornando lista como resultado
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))


