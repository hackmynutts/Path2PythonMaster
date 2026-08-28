import random
# Número que queremos encontrar
objetivo = 10

# -------------------------------
# Crear población inicial
# -------------------------------
poblacion = [
    random.randint(0,20),
    random.randint(0,20),
    random.randint(0,20),
    random.randint(0,20)
]

print("================================")
print("POBLACIÓN INICIAL")
print("================================")
print(poblacion)

# -------------------------------
# Evolución por generaciones
# -------------------------------
for generacion in range(10):
    print("\n\n================================")
    print("GENERACIÓN:", generacion + 1)
    print("================================")

    print("Población actual:")
    print(poblacion)

    # -------------------------------
    # Evaluación de fitness
    # -------------------------------
    print("\nEvaluación de individuos:")
    for individuo in poblacion:
        distancia = abs(objetivo - individuo)
        print(
            "Individuo:",
            individuo,
            "Distancia al objetivo:",
            distancia
        )

    # Buscar el mejor individuo
    mejor = min(
        poblacion,
        key=lambda x: abs(objetivo-x)
    )

    print("\nMejor individuo:")
    print(
        mejor,
        "con distancia:",
        abs(objetivo-mejor)
    )

    # Verificar solución
    if mejor == objetivo:
        print("\n OBJETIVO ENCONTRADO")
        break

    # -------------------------------
    # Crear nueva generación
    # -------------------------------

    print("\nCreando nueva generación...")

    nueva = []

    for numero in poblacion:

        valor_original = numero

        # Mutación sencilla:
        # acercarse al objetivo
        if numero < objetivo:
            numero += 1
        else:
            numero -= 1

        print(
            "Individuo",
            valor_original,
            "genera hijo:",
            numero
        )

        nueva.append(numero)

    print("\nNueva población:")
    print(nueva)

    # Reemplazar población
    poblacion = nueva

print("\n================================")
print("RESULTADO FINAL")
print("================================")
print(
    "Solución encontrada:",
    mejor
)