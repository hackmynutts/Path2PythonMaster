# #la ide a de tener funciones
# #una funcion es un bloque de codigo que se llama cuando se necesita
# #la funcion puede recibir parametros y devolver valores
# # tambien se puede usar para transformar codigo repetido en funciones

print("Ingresa un valor: ")
a = int(input())

print("Ingresa un valor: ")
b = int(input())

print("Ingresa un valor: ")
c = int(input())
#notamos que lo que siempre se repite es el print

def message():
    print("Ingresa un valor: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

#tambien podemos hacerlo con parametros dentro de la funcion

def hello(name):    # definiendo una función
    print("Hello,", name)    # cuerpo de la función


name = input("Ingresa tu nombre: ")

hello(name)    # invocación de la función

#Los parametros solo existen dentro de las funciones
#los argumentos existen fuera de ella 
#se debe de proveer el mismo numero de argumentos que de parametros
#es posible tener una variable del mismo nombre del parametro de la funcion
def message(number):
    print("El numero ingresado fue:", number)

number = int(input("Ingresa un número: "))
message(number)


#parametros posicionales
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Skywalker", "Luke")#lo que cambia es el orden conforme pasamos los argumentos
introduction("Quick", "Jesse")
introduction("Kent", "Clark")


def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)
adding(10, 20, 30)
adding(100, 200, 300)





 