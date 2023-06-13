import random
from queue import LifoQueue as Pila

#1
def contarLineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo)
    lineas: list[str] = archivo.readlines()
    archivo.close()
    return len(lineas)

def existePalabra(palabra: str, nombre_archivo: str) -> bool:
    resultado: bool = False
    archivo = open(nombre_archivo)
    lineas: list[str] = archivo.readlines()
    for i in range(0, len(lineas)):
        if palabra in lineas[i]:
            resultado = True
            break
    archivo.close()
    return resultado

def cantidadApariciones(nombre_archivo: str, palabra: str) -> int:
    resultado: int = 0
    archivo = open(nombre_archivo)
    lineas: list[str] = archivo.readlines()
    for i in range(0, len(lineas)):
        resultado += lineas[i].replace("\n", "").split(" ").count(palabra)
    archivo.close()
    return resultado

#8
def generarNumerosAlAzar(n: int, desde: int, hasta: int) -> list[int]:
    intervalo: list[int] = []
    for i in range(desde, hasta + 1):
        intervalo.append(i)
    return random.sample(intervalo, n)

#9
def armarPila(n: int, desde: int, hasta: int) -> Pila:
    pila: Pila = Pila()
    numeros: list[int] = generarNumerosAlAzar(n, desde, hasta)
    for i in range(0, len(numeros)):
        pila.put(numeros[i])
    return pila

#10
def cantidadElementos(pila: Pila) -> int:
    elementos: list[int] = []
    while (not pila.empty()):
        elementos.append(pila.get())
    resultado: int = len(elementos)
    while (elementos):
        pila.put(elementos.pop())
    return resultado

#11
