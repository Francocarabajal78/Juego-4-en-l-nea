from typing import List

CELDA_VACIA = ' '
CELDA_X = 'X'
CELDA_O = "O"

def crear_tablero(n_filas: int, n_columnas: int) -> List[List[str]]:
    """Crea un nuevo tablero de cuatro en línea, con dimensiones
    n_filas por n_columnas.
    Para todo el módulo `cuatro_en_linea`, las cadenas reconocidas para los
    valores de la lista de listas son las siguientes:
        - Celda vacía: ' '
        - Celda con símbolo X: 'X'
        - Celda con símbolo O: 'O'

    PRECONDICIONES:
        - n_filas y n_columnas son enteros positivos mayores a tres.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero lleno de casilleros vacíos
          que se puede utilizar para llamar al resto de las funciones del
          módulo.

    EJEMPLO:
        >>> crear_tablero(4, 5)
        [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]
    """
    tablero = []
    for fila in range(n_filas):
        tablero.append([])
        for columna in range(n_columnas):
            tablero[fila].append(CELDA_VACIA)
    return tablero


def es_turno_de_x(tablero: List[List[str]]) -> bool:
    """Dado un tablero, devuelve True si el próximo turno es de X. Si, en caso
    contrario, es el turno de O, devuelve False.
    - Dado un tablero vacío, dicha función debería devolver `True`, pues el
      primer símbolo a insertar es X.
    - Luego de insertar el primer símbolo, esta función debería devolver `False`
      pues el próximo símbolo a insertar es O.
    - Luego de insertar el segundo símbolo, esta función debería devolver `True`
      pues el próximo símbolo a insertar es X.
    - ¿Qué debería devolver si hay tres símbolos en el tablero? ¿Y con cuatro
      símbolos?

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
        - los símbolos del tablero fueron insertados previamente insertados con
          la función `insertar_simbolo`"""

    contador_de_simbolos = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if(tablero[fila][columna] != CELDA_VACIA):
                contador_de_simbolos += 1
    if(contador_de_simbolos % 2 == 0 or contador_de_simbolos == 0):
        return True
    return False


def columna_llena(tablero: List[List[str]], columna: int) -> bool:
    """Dado un tablero y un índice de columna, se fija si esa columna está completa,
    si es así, devuelve True.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    
    """
    for i in range(len(tablero)):
        if tablero[i][columna] == CELDA_VACIA:
            return False
    return True

def insertar_simbolo(tablero: List[List[str]], columna: int) -> bool:
    """Dado un tablero y un índice de columna, se intenta colocar el símbolo del
    turno actual en dicha columna.
    Un símbolo solo se puede colocar si el número de columna indicada por
    parámetro es válido, y si queda espacio en dicha columna.
    El número de la columna se encuentra indexado en 0, entonces `0` corresponde
    a la primer columna.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    POSTCONDICIONES:
        - si la función devolvió `True`, se modificó el contenido del parámetro
          `tablero`. Caso contrario, el parámetro `tablero` no se vio modificado
    """

    turno = es_turno_de_x(tablero)

    if columna < 0 or columna >= len(tablero[0]):
        return False    
    if tablero_completo(tablero):
        return False

    if tablero[0][columna] == CELDA_VACIA:
        for fila in range(len(tablero)-1, -1, -1): #Recorre las filas desde abajo
            if(turno and tablero[fila][columna] == CELDA_VACIA):
                tablero[fila][columna] = CELDA_X
                return True
            if(not turno and tablero[fila][columna] == CELDA_VACIA):
                tablero[fila][columna] = CELDA_O
                return True
    else:
        return False



def tablero_completo(tablero: List[List[str]]) -> bool:
    """Dado un tablero, indica si se encuentra completo. Un tablero se considera
    completo cuando no hay más espacio para insertar un nuevo símbolo, en tal
    caso la función devuelve `True`.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    for i in range(len(tablero[0])):
        if tablero[0][i] == CELDA_VACIA:
            return False
    return True


def recorrer_filas(tablero:  List[List[str]]) -> str:
    """Dado un tablero, lo recorre verificando si hay un símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma horizontal.
    Si es así devuelve el símbolo correspondiente.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`    
    
    """
    for i in range(len(tablero)):   
        for j in range(len(tablero[i])):
            if j < len(tablero[0])-3:
                if tablero[i][j] == CELDA_X and tablero[i][j+1] == CELDA_X and tablero[i][j+2] == CELDA_X and tablero[i][j+3] == CELDA_X:
                    return CELDA_X
                if tablero[i][j] == CELDA_O and tablero[i][j+1] == CELDA_O and tablero[i][j+2] == CELDA_O and tablero[i][j+3] == CELDA_O:
                    return CELDA_O


def recorrer_columnas(tablero:  List[List[str]]) -> str:
    """Dado un tablero, lo recorre verificando si hay un símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma vertical.
    Si es así devuelve el símbolo correspondiente.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`    
    
    """
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if i < len(tablero)-3:
                if tablero[i][j] == CELDA_X and tablero[i+1][j] == CELDA_X and tablero[i+2][j] == CELDA_X and tablero[i+3][j] == CELDA_X:
                    return CELDA_X
                if tablero[i][j] == CELDA_O and tablero[i+1][j] == CELDA_O and tablero[i+2][j] == CELDA_O and tablero[i+3][j] == CELDA_O:
                    return CELDA_O



def recorrer_diagonal(tablero:  List[List[str]]) -> str:
    """Dado un tablero, lo recorre verificando si hay un símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma diagonal.
    Si es así devuelve el símbolo correspondiente.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`  
    
    """
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if i < len(tablero)-3 and j < len(tablero[0])-3:
                if tablero[i][j] == CELDA_X and tablero[i+1][j+1] == CELDA_X and tablero[i+2][j+2] == CELDA_X and tablero[i+3][j+3] == CELDA_X:
                    return CELDA_X
                if tablero[i][j] == CELDA_O and tablero[i+1][j+1] == CELDA_O and tablero[i+2][j+2] == CELDA_O and tablero[i+3][j+3] == CELDA_O:
                    return CELDA_O


def recorrer_diagonal_inversa(tablero:  List[List[str]]) -> str:
    """Dado un tablero, lo recorre desde el final verificando si hay un símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma diagonal.
    Si es así devuelve el símbolo correspondiente.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`  
    
    """
    for i in range(len(tablero)-1, -1, -1):
        for j in range(len(tablero[0])):
            if i > 2 and  j < len(tablero[0])-3:
                if tablero[i][j] == CELDA_X and tablero[i-1][j+1] == CELDA_X and tablero[i-2][j+2] == CELDA_X and tablero[i-3][j+3] == CELDA_X:
                    return CELDA_X
                if tablero[i][j] == CELDA_O and tablero[i-1][j+1] == CELDA_O and tablero[i-2][j+2] == CELDA_O and tablero[i-3][j+3] == CELDA_O:
                    return CELDA_O






def obtener_ganador(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el símbolo que ganó el juego.
    El símbolo ganador estará dado por aquel que tenga un cuatro en línea. Es
    decir, por aquel símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma horizontal, vertical, o diagonal.
    En el caso que el juego no tenga ganador, devuelve el símbolo vacío.
    En el caso que ambos símbolos cumplan con la condición de cuatro en línea,
    la función devuelve cualquiera de los dos.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """
    
    ganador_fila = recorrer_filas(tablero)
    ganador_columna = recorrer_columnas(tablero)
    ganador_diagonal = recorrer_diagonal(tablero)
    ganador_diagonal_inversa = recorrer_diagonal_inversa(tablero)

    if ganador_fila:
        return ganador_fila
    if ganador_columna: 
        return ganador_columna
    if ganador_diagonal:
        return ganador_diagonal
    if ganador_diagonal_inversa:
        return ganador_diagonal_inversa
    if tablero_completo(tablero):
        return False
    return CELDA_VACIA
                
     
