#vamos a hacer el juego del tic tac toe
from random import choice
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_board(board):
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

def first_move(board):
    # La función acepta el estado actual del tablero y decide el primer movimiento, 
    # luego actualiza el tablero acorde a la elección.
    print("Primer movimiento de la maquina: \n")
    board[1][1] = "X"
    make_list_of_free_fields(board)
    return board

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    print("Tu turno \n")
    while True:
        user_move = int(input("Ingrese su movimiento: "))
        if 1 <= user_move <= 9:
            if board[0][0] == user_move:
                board[0][0] = "O"
                make_list_of_free_fields(board)
            elif board[0][1] == user_move:
                board[0][1] = "O"
                make_list_of_free_fields(board)
            elif board[0][2] == user_move:
                board[0][2] = "O"
                make_list_of_free_fields(board)
            elif board[1][0] == user_move:
                board[1][0] = "O"
                make_list_of_free_fields(board)
            elif board[1][1] == user_move:
                board[1][1] = "O"
                make_list_of_free_fields(board)
            elif board[1][2] == user_move:
                board[1][2] = "O"
                make_list_of_free_fields(board)
            elif board[2][0] == user_move:
                board[2][0] = "O"
                make_list_of_free_fields(board)
            elif board[2][1] == user_move:
                board[2][1] = "O"
                make_list_of_free_fields(board)
            elif board[2][2] == user_move:
                board[2][2] = "O" 
                make_list_of_free_fields(board)
        else:
            print("Movimiento no valido")
            user_move = int(input("Ingrese su movimiento valido (1-9): "))
            if user_move not in range(1, 10):
                print("Movimiento no valido")
                continue
            else: 
                if board[0][0] == user_move:
                    board[0][0] = "O"
                    make_list_of_free_fields(board)
                elif board[0][1] == user_move:
                    board[0][1] = "O"
                    make_list_of_free_fields(board)
                elif board[0][2] == user_move:
                    board[0][2] = "O"
                    make_list_of_free_fields(board)
                elif board[1][0] == user_move:
                    board[1][0] = "O"
                    make_list_of_free_fields(board)
                elif board[1][1] == user_move:
                    board[1][1] = "O"
                    make_list_of_free_fields(board)
                elif board[1][2] == user_move:
                    board[1][2] = "O"
                    make_list_of_free_fields(board)
                elif board[2][0] == user_move:
                    board[2][0] = "O"
                    make_list_of_free_fields(board)
                elif board[2][1] == user_move:
                    board[2][1] = "O"
                    make_list_of_free_fields(board)
                elif board[2][2] == user_move:
                    board[2][2] = "O" 
                    make_list_of_free_fields(board)
        
        return board

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    try:
        free = ()
        for row in range(3):
            for column in range(3):
                if board[row][column] == "X" or board[row][column] == "O":
                    continue
                else:
                    free += ((row, column),)                    
        return free
    except:
        print("Ha ocurrido un error")

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or \
        (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or \
        (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or \
        (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or \
        (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or \
        (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or \
        (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or \
        (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        print("Ha ganado la maquina!! \n" \
              "Mejor suerte la proxima vez :(")
        sign = True
    elif (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or \
        (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or \
        (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or \
        (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        print("Has ganado!!" \
              "\nFelicidades, le ganaste a la maquina :D")
        sign = True
    elif make_list_of_free_fields(board) != ():
        print("No hay ganador aun. Sigue la cumbia. \n")
        sign = False
    else:
        print("Empate!!" \
              "\nVuelve a intentarlo." \
              "\nAsi quedo la partida: \n")
        display_board(board)
        sign = True
    return sign

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    print("Mueve la maquina: \n")
    lista = list(make_list_of_free_fields(board))
    move = choice(lista)
    board[move[0]][move[1]] = "X"
    make_list_of_free_fields(board)
    return board

inicio_juego= input("*********BIENVENIDOS AL JUEGO DEL GATO********** \n" \
                    "|||||||||||||||||||Tic Tac Toe|||||||||||||||||| \n" 
                    "-------------Diseñado por Jorge MORUA----------- \n" 
                    "Jugaras contra la maquina hasta que gane uno de los dos o bien haya un empate."
                    "Desea iniciar el juego? (S/N): \n")
if inicio_juego == "N":
    exit()
else:
    print("Tablero inicial: \n")
    display_board(board)
    first_move(board)
    display_board(board)
    sign = False
    while sign == False:
        enter_move(board)
        display_board(board)
        sign = victory_for(board, sign)
        if sign == True:
            break
        draw_move(board)
        display_board(board)
        sign =victory_for(board, sign)


