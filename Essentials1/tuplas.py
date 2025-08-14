#tuplas 
#las tuplas son inmutables
#no se puede reasignar un valor a una tupla
#las tuplas se definen con parentesis

numbers = (5,7,32,54,77)
tuple_2 = 1., .5, .25, .125 #con comas solamente tambien
 
print("la tupla de numeros es ", numbers)

print("\nla longitud de la tupla es ", len(numbers))

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
#que no hacer
#my_tuple.append(10000)#nos dara error, ya que las tuplas son inmutables

print(my_tuple)

#tambien podemos trabajar con los siguientes metodos y funciones
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)




var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)


#la unica forma de "modificar" una tupla es convertirla en una lista
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits) #convertimos a lista
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits) #convertimos de vuelta a tupla
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')