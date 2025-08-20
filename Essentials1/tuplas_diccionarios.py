school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in school_class.keys():
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(f"Notas de {name}: {school_class[name]}")
    print(name, ":", adding / counter)

    print(school_class["Bri"])



