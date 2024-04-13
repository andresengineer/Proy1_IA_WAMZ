import tkinter as tk
import time
from tkinter import filedialog, messagebox
# from ClaseNodo import Nodo
import shutil
 

# Lee una matriz desde un archivo de texto.
def leerMatriz(url):
    matriz = []
    with open(url, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()  # Eliminar espacios en blanco y dividir la línea en elementos
            matriz.append(fila)
    return matriz


# Permite al usuario seleccionar un nuevo mundo.
def escogerMundo():
    messagebox.showinfo("Info", "Puede seleccionar uno de los mundos dados, o crear tú propio mundo con una matríz de (10x10).")
    file = filedialog.askopenfilename(title="Escoger Mundo")
    if file:
        yes = tk.messagebox.askyesno("Iniciar nuevo mundo", f"¿Deseas iniciar un nuevo mundo?")
        if yes:
            shutil.copy2(file, "./matriz.txt")
            tk.messagebox.showinfo("Mundo creado", f"Has iniciado un nuevo mundo.")
            print("Mundo seleccionado correctamente")



# Calcula el tiempo de implementación de una funcion.
def tiempoDeEjecucion (funcion):
    # Hora inicio
    inicio = time.time()
    
    # Llamar a la función proporcionada
    funcion()
    
    # Hora fin
    fin = time.time() 
    
    # Diferencia entre tiempos para obtener el tiempo transcurrido
    return fin - inicio



# Función recursiva para verificar si un estado ya ha sido visitado en los nodos anteriores.
def verificarEstadoRepetido(estadoHijo, nodoPadre):
    # Obtener el padre del nodo
    padre = nodoPadre.get_padre()
    
    # Verificar si el nodo es la raíz
    if padre is None:
        return True  # El estado del hijo es diferente a todos los nodos anteriores
    
    # Verificar si el estado del hijo es igual al del padre
    elif estadoHijo == padre.get_estado():
        return False  # # El estado del hijo es igual a uno los nodos anteriores.
    
    else:
        # Llamar recursivamente para revisar al siguiente ancestro
        return verificarEstadoRepetido(estadoHijo, padre)



#Ubicar posición del elemento
def ubicarElemento (matriz, elementoabuscar):
    coordenadas = []
    for fila in matriz:
        for elemento in fila:
            if elemento == elementoabuscar:
                coordenadas.append(matriz.index(fila))
                coordenadas.append(fila.index(elemento))
    if not coordenadas:
        return -1
    return coordenadas



def distanciaManhattan(matriz):
    # Obtener la ubicación de Mando y Grogu en la matriz
    ubicacionMando = ubicarElemento(matriz, '2')
    ubicacionGrogu = ubicarElemento(matriz, '5')
    
    # Verificar si Mando o Grogu no están presentes en la matriz
    if ubicacionMando == -1 or ubicacionGrogu == -1:
        return 0
    
    # Calcular las distancias entre Mando y Grogu
    distancias = []
    sumaDistanciasGrogus = 0
    for i in range(0, len(ubicacionGrogu), 2):
        distancia = abs(ubicacionGrogu[i] - ubicacionMando[0]) + abs(ubicacionGrogu[i + 1] - ubicacionMando[1])
        distancias.append(distancia)
        # Calcular la distancia entre Grogu si hay mas de uno
        if i + 2 < len(ubicacionGrogu):
            sumaDistanciasGrogus += abs(ubicacionGrogu[i] - ubicacionGrogu[i + 2]) + abs(ubicacionGrogu[i + 1] - ubicacionGrogu[i + 3])
    
    # Calcular la distancia total
    distancia_total = min(distancias) + sumaDistanciasGrogus
    
    # Devolver la distancia total
    return distancia_total



