# #tambien podemos crear una matriz con comprension de listas
# matrix = [[x for x in range(3)] for y in range(3)]
# print(matrix)


EMPTY = " "
KNIGHT = "CABALLO"
PAWN = "PEON"
ROOK = "TORRE"
board = [[EMPTY for i in range(8)] for j in range(8)]
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[4][2] = KNIGHT
board[3][4] = PAWN
print(board)


temps = [[0.0 for h in range(24)] for d in range(31)]

print(temps)

#python no limita a las matrices en cuanto a la 
#cantidad de listas dentro de listas que puedan existir
#este es un ejemplo de una matriz de 3 dimensiones
#Imagina un hotel. Es un hotel enorme que consta de tres edificios, 
#de 15 pisos cada uno. 
#Hay 20 habitaciones en cada piso. 
#El hotel necesita procesar información sobre las habitaciones ocupadas/libres.

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print(vacancy)


