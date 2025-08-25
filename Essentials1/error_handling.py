#manejo de errores
#si enviamos un valor no natural o bien nada, el programa se cae
value = int(input('Ingresa un número natural: '))
if type(value) is int:
    print('El recíproco de', value, 'es', 1/value) #ValueError: invalid literal for int() with base 10: ''


#ejemplo de try ... exception
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)
except:
    print('Debes ingresar un número natural')

#tambien podemos trabajar con mas de un tipo de excepcion 
#esto se logra porque usamos el nombre de la excepcion en el except
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)
except ValueError:
    print('Debes ingresar un número natural')
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)
except ZeroDivisionError:
    print('No puedes dividir por cero')

#tambien podemos trabajar con una excepcion default 
# esto se logra porque NO usamos el nombre de la excepcion en el except al final, Y SIEMPRE DEBE DE IR AL FINAL
#el default se ejecuta si no se cumple ninguna de las anteriores
#podemos usar tantas excepciones como queramos siempre y cuando usamos el nombre de la excepcion en el except
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    ('No se que hacer con.')    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except:
    print('Ha sucedido algo extraño, ¡lo siento!')
