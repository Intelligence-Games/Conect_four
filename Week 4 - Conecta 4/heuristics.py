import random


def random_heuristic(state=None):
    return random.randint(-100, 100)




def check_horizontal(state=None):
    fila = 1
    columna = 1
    posicion = (fila, columna)

    for fila in state.board(fila,columna):
        huecos_izq = check_left_consecutive_hole(columna,state.moves)
        rig = check_right_consecutive_hole(columna,state.moves)

def check_left_consecutive_hole(columna,moves):
    fila = 1
    numero_de_huecos = 0
    for fila in moves(fila,columna):
        numero_de_huecos + 1
        fila+1

    print numero_de_huecos;

def check_right_consecutive_hole(player,columna):
    pass



#       Instrucciones !!!
# Tenemos que buscar en la misma columa, hacia arriba cuantas posiciones tienen resultado de "state.board.get(columa,fila)"
# igual a "." Si se encuentra con una ficha del jugador contrario al hacer el "state.board.get(columa,fila)" entonces disminuye
# el valor de esa direccion y si encuentra una hilera de 4 espacios vacios tiene mayor valor. Son mejores las hileras en horizontal,
# despues en vertical y por último las diagonales, porque para hacer un 4 en raya en diagonal necesitas poner muchas más piezas
#si un poco, al principio recorriendo las 7 posibilidades osea la fila 1, recorrer las columnas y preguntar con state.board
#(fila, columna) la posibilidad de cuatro en raya que tiene, y de las 7 posibilidades que tienes de colocar la ficha devolver
#la de mayor valor