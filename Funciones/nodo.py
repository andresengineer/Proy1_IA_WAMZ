from Funciones.funciones import *
import pygame


pygame.mixer.init()


 #  Añade la musica final.
def music():
    pygame.mixer.music.load("../recursos/next.mp3")
    pygame.mixer.music.play(loops=0)

class Nodo:
    #Constructor
    def __init__(self, estado, padre, operador):
        self.estado = estado
        self.padre = padre
        self.operador = operador
        self.costo = 0
        self.enemigo = '0'
        self.nave = 0
        self.heuristicaMasCosto = 0
        self.heuristica = 0
        self.profundidad = 0  


    def __lt__(self, otro_nodo):
        # Define la comparación basada en el costo
        return self.costo < otro_nodo.costo  

    # Getters/Setters

    # Padre
    def get_padre(self):
        return self.padre
    
    def set_Padre(self, nuevopadre):
        self.padre = nuevopadre


    # Estado
    def get_estado(self):
        return self.estado
    
    def set_estado(self, nuevoEstado):
        self.estado = nuevoEstado


    # Operador
    def get_operador(self):
        return self.operador
    
    def set_operador(self, nuevoOperador):
        self.operador = nuevoOperador


    # Costo
    def get_costo(self):
        return self.costo
    
    def set_costo(self, nuevoCosto):
        self.costo = nuevoCosto


    # Enemigo
    def get_enemigo(self):
        return self.enemigo
    
    def set_enemigo(self, nuevoEnemigo):
        self.enemigo = nuevoEnemigo

    
    # Nave
    def get_nave(self):
        return self.nave
    
    def set_nave(self, nuevaNave):
        self.nave = nuevaNave


    # Heuristica
    def get_heuristica(self):
        return self.heuristica
    
    def set_heuristica(self,nuevaHeuristica):
        self.heuristica = nuevaHeuristica  

    
    # Heuristica + Costo
    def get_heuristicaCosto(self):
        return self.heuristicaMasCosto
    
    def set_HeuristicaCosto(self, heuristica_costo):
        self.heuristicaMasCosto = heuristica_costo

    
    # Profundidad
    def get_profundidad(self):
        return self.profundidad
    
    def set_profundidad(self, nuevaProfundidad):
        self.profundidad = nuevaProfundidad    


   

   
    # Calcula y devuelve una lista de movimientos válidos para desplazar el elemento actual en el juego.
    def moverse(self):
        music()
        # Obtener el estado actual del juego
        estadoActual = self.estado
        
        # Personaje
        elemento = ubicarElemento(estadoActual, '2')
        fila = elemento[0]
        columna = elemento[1]

        # Definir las direcciones posibles y sus operadores asociados
        direcciones = [(0, 1, "derecha"), (0, -1, "izquierda"), (-1, 0, "subir"), (1, 0, "bajar")]

        # Inicializar la lista de movimientos válidos
        movimientos = []
        
        # Inicializar la variable para almacenar el enemigo
        enemigo = '0'

        # Recorrer cada posible movimiento: derecha, izquierda, arriba, abajo
        for dr, dc, operador in direcciones:
            nueva_fila = fila + dr
            nueva_columna = columna + dc
            
            # Verificar si el movimiento es válido
            if 0 <= nueva_fila < len(estadoActual) and 0 <= nueva_columna < len(estadoActual[0]) and estadoActual[nueva_fila][nueva_columna] != '1':
                # Copiar el estado actual para no modificarlo directamente
                matrizActual = [fila[:] for fila in estadoActual]

                # Si encuentra una nave
                if matrizActual[nueva_fila][nueva_columna] == '3':
                    # Incrementar la cantidad de gasolina en 10
                    nave = self.nave + 10
                    # Actualizar la matriz con el movimiento
                    matrizActual[nueva_fila][nueva_columna] = '2'
                    matrizActual[fila][columna] = self.enemigo
                    # Incrementar el costo solo si hay gasolina disponible

                    if self.nave > 0:
                        self.costo = self.padre.costo + 0.5
                    # La nave proporciona inmunidad contra los enemigos
                    enemigo = '0'

                # Si el elemento es un enemigo
                elif matrizActual[nueva_fila][nueva_columna] == '4':
                    # Si no hay gasolina en la nave

                    

                    if self.nave <= 0:
                        # Guardar el tipo de enemigo
                        enemigo = matrizActual[nueva_fila][nueva_columna]
                        # Guardar el estado de la gasolina
                        nave = self.nave
                        # Actualizar la matriz con el movimiento
                        matrizActual[nueva_fila][nueva_columna] = '2'
                        matrizActual[fila][columna] = self.enemigo

                    else:
                        # Reducir la gasolina en cada movimiento
                        nave = max(self.nave - 1, 0)  # Asegurar que la gasolina no sea negativa
                        # Guardar el valor del enemigo
                        enemigo = '0'
                        # Actualizar la matriz con el movimiento
                        matrizActual[nueva_fila][nueva_columna] = '2'
                        # Cuando la nave está presente, el enemigo desaparecerá definitivamente
                        matrizActual[fila][columna] = '0'

                # Si no hay ni nave ni enemigo en la casilla
                else:
                    # Actualizar la matriz con el movimiento
                    matrizActual[nueva_fila][nueva_columna] = '2'
                    matrizActual[fila][columna] = self.get_enemigo()  
                    # El enemigo será cero
                    enemigo = '0' 
                    # Reducir la gasolina en cada movimiento
                    nave = max(self.nave - 1, 0)  # Asegurar que la gasolina no sea negativa

                    # Incrementar el costo si la nave tiene gasolina disponible
                    if self.nave > 0:
                        self.costo = self.padre.costo + 0.5
                            
                # Agregar la actualización al arreglo    
                movimientos.append((matrizActual, operador, nave, enemigo))

        # Devolver la lista de movimientos válidos
        return movimientos


    # Aumentar la profundidad del nodo.
    def aumentarProfundidad(self):
        if self.padre is not None:
            self.profundidad = self.padre.profundidad + 1
   

    # Aumentar el costo si se encuentra un enemigo.
    def aumentarCosto (self):
        if self.get_enemigo() == '4':
            self.costo = self.padre.costo + 5
        else:
            self.costo = self.padre.costo + 1

           
    # Determina si la matriz dada contiene a Grogu.
    def encontroGrogu (self, matriz):
        #Si la matriz no contiene esferas, es meta
        return ubicarElemento(matriz,'5') == -1
    
    def sumaTotal(self):
        self.heuristicaMasCosto = self.costo + self.heuristica 
                 