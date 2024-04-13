import tkinter as tk
from customtkinter import *
from tkinter import StringVar, PhotoImage
from Funciones.funciones import escogerMundo
import os
import pygame

root = CTk()
pygame.mixer.init()


width = root.winfo_screenwidth()
height = root.winfo_screenheight()

x = int((width - 700) / 2)
y = int((height - 600) / 2)


# Cargar Imagenes.
fondo = PhotoImage(file="images/fondo3.png")

# Añadir Imagenes a la ventana principal.
fondo_label = tk.Label(root, image=fondo, border=0)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Configuración de la ventana.
root.geometry(f"712x400+{x}+{y}")
root.title("Smart Mandalorian")
root.resizable(False, False)
set_default_color_theme("green")

# llamar funciones

# Selecciona el algoritmo de busqueda deseado.
def elegirAlgoritmo(event):
    if event == "Amplitud" or event == "Costo" or event == "Profundidad":
        opciones = noInformada.get()
    elif event == "Avara" or event == "Estrella":
        opciones = informada.get()

    os.chdir(opciones)  # Cambiar al directorio especificado
    comando = "python main.py"  
    if opciones:
        root.destroy()
        os.system(comando)


# Botones
botonSeleccionar = CTkButton(root, text="Seleccionar Mundo", command=escogerMundo, font=("Georgia", 18), width=150, height=50)
botonSeleccionar.place(relx=0.47, x=-botonSeleccionar.winfo_reqwidth()/2, rely=0.4, y=-botonSeleccionar.winfo_reqheight()/2)

#labels
labelAlgoritmo = CTkLabel(root, text="Seleccionar algorítmo de búsqueda", fg_color="#001d49", justify="center", anchor="center", font=("Georgia", 20), height=50, width=100)
labelAlgoritmo.place(relx=0.36, x=-botonSeleccionar.winfo_reqwidth()/2, rely=0.65, y=-botonSeleccionar.winfo_reqheight()/2)


def musicFinal():
    pygame.mixer.music.load("../recursos/r2d2.mp3")
    pygame.mixer.music.play(loops=0)


# Crear los menús de selección

# Algoritmo de busqueda NO informada
noInformada = StringVar(value="Busqueda No Informada")
menu1 = CTkOptionMenu(root,values=["Amplitud", "Costo", "Profundidad"],
                                         command=elegirAlgoritmo,
                                         variable=noInformada,
                                         width=150, height=50,
                                         font=("Georgia", 15))

menu1.place(x=105, y=300)

# Algoritmo de busqueda informada
informada = StringVar(value="Busqueda Informada")
menu2 = CTkOptionMenu(root,values=["Avara", "Estrella"],
                                         command=elegirAlgoritmo,
                                         variable=informada,
                                         width=150, height=50,
                                         font=("Georgia", 15))

menu2.place(x=360, y=300)


root.mainloop()


