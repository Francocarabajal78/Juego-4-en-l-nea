lista = [[1,2,3],[4,5,6],[7,8,9]]

def pintar_tablero(tablero):
    for fila in range(len(tablero)):
        print(fila)
        for col in range(len(tablero[fila])):
            print(tablero[fila][col], end=" | ")
        print(" ")




def obtener_ganador_desde_posicion(tablero, fila, columna):
    """
    Dado un tablero, su fila y su columna, devuelve el simbolo que se repite cuatro veces consecutivas a esa posición
    en cada dirección.
    En el caso de que no se repita ningún símbolo devuelve 'None'.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    if recorrer_filas(tablero, fila) == "X" or recorrer_columnas(tablero, columna) == "X" or recorrer_diagonal(tablero, fila, columna) == "X":
        return "X"
    elif recorrer_filas(tablero, fila) == "O" or recorrer_columnas(tablero, columna) == "O" or recorrer_diagonal(tablero, fila, columna) == "O":
        return "O"





        





def recorrer_filas(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if j < len(tablero[0])-3:
                if tablero[i][j] == "X" and tablero[i][j+1] == "x" and tablero[i][j+2] == "X" and tablero[i][j+3] == "X":
                    return "X"
                if tablero[i][j] == "O" and tablero[i][j+1] == "O" and tablero[i][j+2] == "O" and tablero[i][j+3] == "O":
                    return "O"

def recorrer_columnas(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if i < len(tablero)-3:
                if tablero[i][j] == "X" and tablero[i+1][j] == "x" and tablero[i+2][j] == "X" and tablero[i+3][j] == "X":
                    return "X"
                if tablero[i][j] == "O" and tablero[i+1][j] == "O" and tablero[i+2][j] == "O" and tablero[i+3][j] == "O":
                    return "O"

def recorrer_diagonal(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if i < len(tablero)-3 and j < len(tablero[0])-3:
                if tablero[i][j] == "X" and tablero[i+1][j+1] == "X" and tablero[i+2][j+2] == "X" and tablero[i+3][j+3] == "X":
                    return "X"
                if tablero[i][j] == "O" and tablero[i+1][j+1] == "O" and tablero[i+2][j+2] == "O" and tablero[i+3][j+3] == "O":
                    return "O"


def recorrer_diagonal_inversa(tablero):
    for i in range(len(tablero)-1, -1, -1):
        for j in range(len(tablero[0])):
            if i > 2 and  j < len(tablero[0])-3:
                print(tablero[i][j])
                if tablero[i][j] == "X" and tablero[i-1][j+1] == "X" and tablero[i-2][j+2] == "X" and tablero[i-3][j+3] == "X":
                    return "X"
                if tablero[i][j] == "O" and tablero[i-1][j+1] == "O" and tablero[i-2][j+2] == "O" and tablero[i-3][j+3] == "O":
                    return "O" 




def mostrar_ultima_casilla(tablero):
    for i in range(len(tablero[0])):
        print(tablero[0][i])


tablero_prueba = [
            ['O', ' ', 'X', ' ', ' '],
            [' ', ' ', ' ', 'X', ' '],
            [' ', ' ', 'X', 'O', ' '],
            ['O', 'X', 'X', 'X', ' '],
            ['X', 'O', 'O', 'O', ' ']]

            

"""
def palindromos(frase):
    frase_2 = ""
    for p in frase.split():
        frase_2 += p
   
    if "".join(frase.lower().split()) == frase_2[::-1].lower():
        return True
    return False
"""        

