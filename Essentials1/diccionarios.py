#diccionarios
# sintaxis para crear un diccionario
# my_dict = {key1: value1, key2: value2, key3: value3}
# diccionarios son colecciones de pares clave-valor donde las claves son unicas y los valores pueden ser duplicados

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
contactos = {'Mami': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

# print(dictionary)
# print(phone_numbers)
# print(empty_dictionary)

# print(phone_numbers['Suzy'])
# print(phone_numbers['suzy']) # KeyError: 'suzy'


#metodo keys 
#devuelve una lista con todas las claves
# 
for key in contactos.keys():
    print(f"Keys: {key} ->  Values: {contactos[key]}") 


#metodo values
#devuelve una lista con todos los valores
for value in contactos.values():
    print("Values: ", value)

#modificar un valor
contactos["Mami"] = 71100938 #atraves de su clave simplemente reemplazamos el valor
print(dictionary)

#agregar un nuevo par clave-valor
contactos["Papi"] = 70122803
print(contactos)

#metodo .update() 
#permite agregar pares clave-valor a un diccionario existente
contactos.update({"Brittany": 71317982, "Rudy": 71317982})
print(contactos)

#eliminar un par clave-valor
del contactos["Rudy"]
print(contactos)

#metodo .copy()
#permite copiar un diccionario
new_dictionary = contactos.copy()
print(new_dictionary)

#eliminar el ultimo par clave-valor
contactos.popitem()
print(contactos)

#eliminar todos los pares clave-valor
contactos.clear()
print(contactos)


#comprobar si una clave esta en un diccionario
print("Brittany" in new_dictionary)
print("Rudy" in new_dictionary)

#comprobar con un valor si esta en un diccionario no funciona
print(71317982 in new_dictionary)#retornara un falso incorrecto, porque 71317982 es un valor y no una clave
