#diccionarios
# sintaxis para crear un diccionario
# my_dict = {key1: value1, key2: value2, key3: value3}
# diccionarios son colecciones de pares clave-valor donde las claves son unicas y los valores pueden ser duplicados

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(phone_numbers['Suzy'])
print(phone_numbers['suzy']) # KeyError: 'suzy'


#metodo keys 
#devuelve una lista con todas las claves
# 
for key in dictionary.keys():
    print(key, "->", dictionary[key])

