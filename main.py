from cuatro_en_linea import crear_tablero, insertar_simbolo, es_turno_de_x, obtener_ganador

def validar_entero(numero: str) -> bool:
    """
    Recibe un número e indica si es entero positivo.
    Si es así, devuelve 'True'.
    """
    if not numero.isdigit() or int(numero) <= 3:
        return False
    return True

def pintar_tablero(tablero: list):
    """
    Dado un tablero, lo imprime de una manera mas agradable a la vista del usuario
    No devuelve un valor.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """

    for columna in range(len(tablero[0])):
        print(f"{columna}", end="|")
    print(" ")
    for _ in range(len(tablero[0])):
        print("-", end="-")
    print(" ")
    for fila in range(len(tablero)):
        for col in range(len(tablero[fila])):
            print(tablero[fila][col], end="|")
        print(" ")



def main():
    mensaje_juego_terminado = "Juego Finalizado."
    print("BIENVENIDO AL 4 EN LÍNEA")
    filas = input("Ingrese la cantidad de filas que tendrá el tablero: ")
    columnas = input("Ingrese la cantidad de columnas que tendrá el tablero: ")
    while True:
        if validar_entero(filas) and validar_entero(columnas):
            break
        print("Parametros inválidos")
        filas = input("Reingrese la cantidad de filas: ")
        columnas = input("Reingrese la cantidad de columnas: ")

    tablero_principal = crear_tablero(int(filas), int(columnas))
    while True:
        pintar_tablero(tablero_principal)
        ganador = obtener_ganador(tablero_principal)
        if ganador != ' ':
            print(f"El ganador es: {ganador}")
            break
        if es_turno_de_x(tablero_principal):
            print("Turno de X")
        else:
            print("Turno de O")
        columna_a_insertar = input("Ingrese la columna / 's' para salir: ")
        if columna_a_insertar == 's' or columna_a_insertar == 'S':
            print(mensaje_juego_terminado)
            return -1
        while True:
            if columna_a_insertar.isdigit():
                break
            columna_a_insertar = input("Entrada inválida, reingrese el valor: ")
        insertar_simbolo(tablero_principal, int(columna_a_insertar))


main()