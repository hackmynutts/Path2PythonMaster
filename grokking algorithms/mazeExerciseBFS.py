from collections import deque

laberinto = [
    "S..#..",
    "##.#.#",
    "......",
    ".####.",
    "....#E",
]

def pasos_minimos(laberinto):
    # 1. Encontrar la posición de la S
    for fila in range(len(laberinto)):
        for col in range(len(laberinto[fila])):
            if laberinto[fila][col] == 'S':
                inicio = (fila, col)

    # 2. Preparar la cola y los visitados
    cola = deque([(inicio, 0)])
    visitados = {inicio}

    # 3. Procesar la cola
    while cola:
        (fila, col), distancia = cola.popleft()

        # 4. Llegue a la salida?
        if laberinto[fila][col] == 'E':
            return distancia

        # 5. Revisar los 4 vecinos
        for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nf, nc = fila + df, col + dc

            dentro = 0 <= nf < len(laberinto) and 0 <= nc < len(laberinto[0])
            if dentro and laberinto[nf][nc] != '#' and (nf, nc) not in visitados:
                visitados.add((nf, nc))
                cola.append(((nf, nc), distancia + 1))

    # 6. La cola se vacio sin encontrar la E
    return -1

print(f"La cantidad de pasos que tomo para llegar a la salida fue de: {pasos_minimos(laberinto)}") #9
print(pasos_minimos(["S.#", "###", "..E"]))  # -1
print(pasos_minimos(["SE"]))                 # 1

