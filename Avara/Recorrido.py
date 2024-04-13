import os, sys
directorio = os.path.dirname(os.path.abspath('../Funciones/funciones.py'))
directorioPadre = os.path.dirname(directorio)
sys.path.append(directorioPadre)
from Funciones.funciones import leerMatriz, tiempoDeEjecucion, verificarEstadoRepetido, distanciaManhattan
from Funciones.nodo import Nodo
import heapq


# Leer matriz desde el archivo.
matriz = leerMatriz("..\matriz.txt")

# Definición de variables
cola = []  # Almacena los nodos hijos
expandidos = []  # Almacena los nodos expandidos


# Busca y extrae el nodo con el menor valor de heuristica.
def obtenerMenorHeuristica():
    nodo_menor_heuristica = min(cola, key=lambda x: x.get_heuristica())
    return cola.pop(cola.index(nodo_menor_heuristica))


# Verifica si el nodo es una solución comprobando si encontró a Grogu en su estado.
def esSolucion(nodo):
    return nodo.encontroGrogu(nodo.estado)

# Genera los nodos hijos a partir de un nodo.
def generarHijos(padreExpandido):
    hijos = []
    for matrizHijos, operador, naves, enemigo in padreExpandido.moverse():    
        # Crea el nodo hijo
        hijo = Nodo(matrizHijos, padreExpandido, operador)
        # Genera los enemigos
        hijo.set_enemigo(enemigo)
        # Genera las naves
        hijo.set_nave(naves)
        # Aumenta el costo de los nodos hijo.
        hijo.aumentarCosto()
        # Aumenta la profundidad del nodo en 1.
        hijo.aumentarProfundidad()
        # Calcula la distancia Manhattan.
        heuristica = distanciaManhattan(matrizHijos)
        # Definir la heuristica.
        hijo.set_heuristica(heuristica)

        es_raiz = padreExpandido.profundidad == 0
        diferente_del_padre = verificarEstadoRepetido(hijo.get_estado(), padreExpandido)

        # Si el nodo es la raíz o si el estado del hijo es diferente al estado del nodo padre. 
        if es_raiz or diferente_del_padre:
            # Agreguelo a la lista de hijos
            hijos.append(hijo)
    return hijos


# Expandir los nodos en el espacio de búsqueda para encontrar la solución.
def expandirNodos ():
    #Definir padre inicial
    padre = Nodo(matriz,None,None)
    #Agregar padre a la cola
    cola.append(padre)
    #Variable que contendrá el primer elemeto de la cola, es decir el padre
    padreExpandido = 0

    #Ejecute mientras la cola este llena
    while cola:
 
        #Sacar el nodo con menor costo y almacenarlo en la variable padre_expandido    
        padreExpandido = obtenerMenorHeuristica()

        # Verificar si el nodo es solucion
        if esSolucion(padreExpandido):
            # Añadir el nodo solucion a la lista expandidos
            expandidos.append(padreExpandido)
            return

        # Crear hijos y agregarlos a la cola
        for hijo in generarHijos(padreExpandido):
            # Agreguelo al final de la cola
            cola.append(hijo)

        #Agregar padre a la lista de nodos espandidos
        expandidos.append(padreExpandido)    

#Guardar tiempo en la variable 
tiempoTotal = tiempoDeEjecucion(expandirNodos)
