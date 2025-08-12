#Funciones con 2 parametros
# Creacion del IMC indice de masa corporal

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb):
    return lb * 0.4535923
 
 
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2
 

weight = float(input("Ingresa el peso: "))
height = float(input("Ingresa la altura: "))
print(bmi(weight, height))
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))


#ahora veamos con tres parametros
#como verificar si es un triangulo
#la suma arbitraria de dos lados tiene que ser mayor que la longitud del tercer lado
# version larga
# def is_a_triangle(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True

#version corta
# def is_a_triangle(a, b, c):
#     if a + b <= c or b + c <= a or c + a <= b:
#         return False
#     return True

#version aun mas compacta
#la suma arbitraria de dos lados tiene que ser mayor que la longitud del tercer lado
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')


#verificar si es un triangulo rectangulo 
#como saber si es un triangulo rectangulo?
#el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos
# hipotenusa**2 = cateto1**2 + cateto2**2
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2 # al estar retornando el valor de la operacion se 
                                         # puede determinar si es o no un triangulo rectangulo
                                         # ya que es una igualdad cuadratica
    if b > a and b > c:
        return b ** 2 == a ** 2 + c ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

#calcular el area de un triangulo
#formula de heron
#semiperimetro p = (a + b + c) / 2
#area = (p * (p - a) * (p - b) * (p - c)) ** 0.5 !!!! raiz cuadrada
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
 
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
 
 
print(area_of_triangle(1., 1., 2. ** .5))