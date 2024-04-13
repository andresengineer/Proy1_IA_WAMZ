import tkinter as tk
from tkinter import PhotoImage
from customtkinter import *
from PIL import Image, ImageTk
from Recorrido import tiempoTotal, expandidos, matriz
from Funciones.nodo import Nodo
import os
import time
import pygame



root = CTk()
pygame.mixer.init()

ancho_pantalla = root.winfo_screenwidth()
altura_pantalla = root.winfo_screenheight()

x = int((ancho_pantalla - 1000) / 2)
y = int((altura_pantalla - 800) / 2)

BLACK = "#010101"
YELLOW = (255, 205, 104)
WHITE = (255, 255, 255) 

fondo3 = PhotoImage(file="../images/fondoA2.png")



# Configuración de la ventana.
root.geometry(f"1090x680+{x}+{y}")
root.title("Costo")
root.resizable(False, False)
set_default_color_theme("blue")

gracias = PhotoImage(file="../images/fondoF.png")



# Añadir Imagenes a la ventana principal.
fondo_label = tk.Label(root, image=fondo3)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
gracias_label = tk.Label(root, image=gracias, border=0)


# Configuracion de la celda
ancho_celda = 60
alto_celda = 60

# Titulo.
labelAlgoritmo = CTkLabel(root, text="ALGORITMO POR COSTO", fg_color="#7c149c", text_color="black", anchor="center", height=50, width=50, font=("Georgia", 32, "bold"))
labelAlgoritmo.place(x= 70, y = 10)


# Función para crear imágenes y agregarlas al mundo
def crearImagenes(canvas, url, label, x, y, width, height):
    imagen = Image.open(url)
    imagen = imagen.resize((x, y))
    imagen = ImageTk.PhotoImage(imagen)
    canvas.create_image(width, height, anchor=tk.NW, image=imagen, tag=label)
    canvas.imagenes.append(imagen)

# Función para dibujar y actualizar el mundo en la pantalla
def dibujarMundo(matriz, canvas, url, etiqueta):
    # Borramos todo lo dibujado anteriormente
    canvas.delete(etiqueta)
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == '1':
                crearImagenes(canvas, url[0], etiqueta, 60, 60, j*ancho_celda, i*alto_celda)
            elif valor == '2':
                crearImagenes(canvas, url[1], etiqueta, 55, 55, j*ancho_celda, i*alto_celda)
            elif valor == '3':
                crearImagenes(canvas, url[2], etiqueta, 55, 55, j*ancho_celda, i*alto_celda)
            elif valor == '4':
                crearImagenes(canvas, url[3], etiqueta, 40, 45, j*ancho_celda, i*alto_celda)
            elif valor == '5':
                crearImagenes(canvas, url[4], etiqueta, 55, 55, j*ancho_celda, i*alto_celda)

# Crear el canvas para representar el mundo
mundo = tk.Canvas(root, width=ancho_celda*10, height=alto_celda*10)
mundo.place(x=60, y=60, width=ancho_celda*10, height=alto_celda*10)

# Dibujar las líneas para representar las celdas del mundo
for i in range(10):
    mundo.create_line(i*ancho_celda, 0, i*ancho_celda, alto_celda*10) 
    mundo.create_line(0, i*alto_celda, ancho_celda*10, i*alto_celda) 

# Lista para almacenar las imágenes del mundo
mundo.imagenes = []

# URL de las imágenes
urlImagenes = ["../images/tile.png", "../images/mando.png", "../images/nave.png", "../images/Stormtroopers2.png", "../images/grogu.png"]

# Ver la matriz inicial del mundo
def verMatrizInical():
    dibujarMundo(matriz, mundo, urlImagenes, 'imagen')

verMatrizInical()

# Obtiene los caminos desde el nodo final hasta la raíz.
def obtenerCaminos(expandidos):
    nodo_actual = expandidos[-1]  # Último nodo expandido
    caminos = []
    while nodo_actual.padre is not None:
        caminos.append(nodo_actual.estado)
        nodo_actual = nodo_actual.padre
    caminos.append(expandidos[-1].estado)  # Agregar el estado final
    caminos_final = caminos[::-1]  # Invertir la lista para obtener los caminos desde la raíz hasta el final
    return caminos_final

camino_final = obtenerCaminos(expandidos)  # Obtener los caminos finales


#  Añade la musica final.
def musicFinal():
    pygame.mixer.music.load("../recursos/r2d2.mp3")
    pygame.mixer.music.play(loops=0)


# Muestra las estadisticas en una ventana.
def estadisticas():
    gracias_label.place(x= 660, y = 60)
    musicFinal()
    tab_wiew = CTkTabview(root, width = 350, height = 200)
    tab_wiew.place(x= 703, y = 250)

    tab_wiew.add("Nodos")
    tab_wiew.add("Profundidad")
    tab_wiew.add("Tiempo")
    tab_wiew.add("Costo")

    nodosExpandidos = str(len(expandidos))
    label = CTkLabel(tab_wiew.tab("Nodos"), text="El número de nodos expandidos es: " + nodosExpandidos, font=("Georgia", 15))
    label.place(x=10, y= 50)

    profundidad = str(expandidos[len(expandidos)-1].profundidad)
    label = CTkLabel(tab_wiew.tab("Profundidad"), text="La profundidad del nodo es: " + profundidad, font=("Georgia", 20))
    label.place(x=35, y= 50)

    tiempoR = "{:.3f}".format(tiempoTotal)
    label = CTkLabel(tab_wiew.tab("Tiempo"), text="El tiempo de cómputo fue: " + tiempoR, font=("Georgia", 18))
    label.place(x=40, y= 50)

    costo = str(expandidos[len(expandidos)-1].costo)
    label = CTkLabel(tab_wiew.tab("Costo"), text="El costo de la solución es : " + costo, font=("Georgia", 20))
    label.place(x=40, y= 50)

# Inicia el juego.
def jugar():
    print("Entrando...")
    etiqueta = 'imagen'  # Etiqueta para identificar la imagen en el canvas
    for matriz in camino_final[1:]:
        dibujarMundo(matriz, mundo, urlImagenes, etiqueta)
        time.sleep(0.1)
        root.update()
    print("Ganaste!")
    estadisticas()

# Vuelve al menú inicial.
def atras ():
    root.destroy()
    os.system("cd ../ && python main.py") 


# Botones
botonJugar = CTkButton(root, text="Jugar", command=jugar, width=150, height=50, hover_color=("#200c1c"), font=("Georgia", 30))
botonJugar.place(x = 700, y = 600)

botonAtras = CTkButton(root, text="Atras", command=atras, width=150, height=50, hover_color=("#200c1c"), font=("Georgia", 30))
botonAtras.place(x = 900, y = 600)

root.mainloop()

