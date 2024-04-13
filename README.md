# Proyecto 1:  Smart Mandalorian. 
### Estudiante:
- Wilson Andrés Mosquera Zapata ( 2182116 )

El objetivo de Mando es encontrar a Grogu en un espacio de 10x10 casillas usando algoritmos de inteligencia artificial. En el ambiente se tiene una nave que Mando puede usar para ir más rápido. También hay enemigos que afectan el estado del agente.


## Algoritmos de búsqueda

Mando, nuestro personaje encuentra la meta usando los siguientes algoritmos de búsqueda:

1. Búsquedas no informadas:

- Preferente por amplitud.
- Preferente por profundidad evitando ciclos.
- De costo uniforme.

2. Búsquedas informadas:

- Avara.
- A\*.

## Como Jugar

### Smart Mandalorian. 

En cada búsqueda que emprenda Mando, este podrá realizar desplazamientos simples tales como moverse arriba, abajo, izquierda, y derecha. El costo de cada movimiento es 1. Si Mando va en la nave, el costo de cada movimiento será 1/2 y además podrá pasar por las casillas donde haya enemigos sin que lo afecten. La nave solo tiene combustible para 10 casillas.
Si Mando llega a una casilla donde hay un enemigo y no va en la nave, el costo será 5 (allí está incluido el costo del movimiento y del daño ocasionado por el enemigo). En el ambiente siempre hay una sola nave, pero la cantidad de enemigos puede variar.
La información del mundo se representa por medio de los siguientes números:

- 0 si es una casilla libre
- 1 si es un muro
- 2 si es el punto de inicio
- 3 si es la nave
- 4 si es un enemigo
- 5 si es Grogu

Por ejemplo para este mundo 

3 0 0 0 0 1 1 0 0 5<br>
0 1 1 1 0 1 1 4 1 4<br>
0 1 0 0 4 4 4 0 1 4<br>
2 0 0 1 1 1 0 1 1 4<br>
0 1 0 4 4 0 0 1 1 4<br>
0 1 0 1 1 1 0 1 1 4<br>
3 0 0 0 1 1 1 0 0 4<br>
1 1 1 0 0 1 0 0 1 0<br>
1 1 1 1 0 0 0 1 0 0<br>
1 1 1 1 1 1 1 1 0 1<br>


El juego iniciará y tu podrás elegir entre los distintos Mundos o crear tu propio mundo como el mostrado en la matriz anterior.


Para poder ver los distintos tipos de algoritmos podra seleccionarlo en un menu desplegable y una vez terminado el recorrido podra ver las estadisticas del algoritmo seleccionado.



### Git clone
```
git clone https://github.com/andresengineer/Proy1_IA_WAMZ.git
```


### Ejecución 
Para ejecutar el archivo ```main.py```, se debe ubicar en la carpeta del programa y ejecutar el siguiente comando:
```bash
python main.py run
```
