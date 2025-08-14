# Exercises: Level 1
# Create an empty tuple
# Create a tuple containing names of your sisters 
#                   and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
# Modify the siblings tuple and add the name of your father and mother 
#                   and assign it to family_members
# Unpack siblings and parents from family_members

empty = ()
tios = ("Jose Roberto", "Alex", "Christian")
tias = ("Andrea", )
print(tios)
print(tias)

familiares = tios + tias
print(familiares)
print("Cuantos familiares hay: ", len(familiares))

tios = list(tios)
tios.insert(0,"Mario")
tios = tuple(tios)
tias = list(tias)
tias.append("Katiana")
tias = tuple(tias)
familia = tios + tias
print(familia)

tiosas = familia[1:5]
papas = familia[0:1] + familia[5:]
print("Tios: ",tiosas)
print("Papas: ",papas)