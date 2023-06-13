from queue import Queue as Cola
from queue import LifoQueue as Pila
from random import randint
from random import sample

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
# def generarNumerosAlAzar(n: int, desde: int, hasta: int) -> list[int]:
#     resultado: list[int] = []
#     for i in range(0, n):
#         resultado.append(randint(desde, hasta))
#     return resultado

def generarNumerosAlAzar(n: int, desde: int, hasta: int) -> list[int]:
    intervalo: list[int] = []
    for i in range(desde, hasta + 1):
        intervalo.append(i)
    return sample(intervalo, n)

#9
def armarPila(n: int, desde: int, hasta: int) -> Pila:
    pila: Pila = Pila()
    numeros: list[int] = generarNumerosAlAzar(n, desde, hasta)
    for i in range(0, len(numeros)):
        pila.put(numeros[i])
    return pila

#10
# def cantidadElementos(pila: Pila) -> int:
#     elementos: list[int] = []
#     while not pila.empty():
#         elementos.append(pila.get())
#         #print(elementos)
#     resultado: int = len(elementos)
#     while elementos:
#         pila.put(elementos.pop())
#         #print(elementos)
#     return resultado

def obtenerElementos(pila: Pila) -> list[int]:
    elementos: list[int] = []
    while not pila.empty():
        elementos.append(pila.get())
    for e in reversed(elementos):
        pila.put(e)
    #print(elementos)
    return elementos

def cantidadElementos(pila: Pila) -> int:
    return len(obtenerElementos(pila))

#11
def buscarMaximo(pila: Pila) -> int:
    return max(obtenerElementos(pila))

#12
def bienBalanceada(string: str) -> bool:
    balance: int = 0
    for c in string:
        if c == "(":
            balance += 1
        elif c == ")":
            balance -= 1
            if balance < 0:
                break
    return balance == 0

#13
def armarCola(n: int, desde: int, hasta: int) -> Cola:
    cola: Cola = Cola()
    numeros: list[int] = generarNumerosAlAzar(n, desde, hasta)
    while numeros:
        cola.put(numeros.pop(0))
    return cola

#14
def cantidadElementos(cola: Cola) -> int:
    elementos: list[int] = []
    while not cola.empty():
        elementos.append(cola.get())
        #print(elementos)
    resultado: int = len(elementos)
    while elementos:
        cola.put(elementos.pop(0))
        #print(elementos)
    return resultado