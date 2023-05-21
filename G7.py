import math

#1
def raizDe2() -> float:
    return round(math.sqrt(2), 4)

def imprimir_hola():
    print("hola")

def imprimir_un_verso():
    print("""
Entonces es como dar amor
Y la distancia no me llegará, amor
Entonces es como dar amor
Y la distancia no me llegará, amor
Y es que te quiero de verdad
Si es que te siento de verdad
""")

def factorial_2() -> int:
    return 2

def factorial_3() -> int:
    return 3 * factorial_2()

def factorial_4() -> int:
    return 4 * factorial_3()

def factorial_5() -> int:
    return 5 * factorial_4()

#2
def imprimir_saludo(nombre: str) -> str:
    print("Hola " + nombre)

def raiz_cuadrada_de(numero: int) -> int:
    return math.sqrt(numero)

def imprimir_dos_veces(estribillo: str):
    print(estribillo * 2)

def es_multiplo_de(n: int, m: int) -> bool:
    return n % m == 0

def es_par(numero: int) -> bool:
    return es_multiplo_de(numero, 2)

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    return math.ceil(comensales * min_cant_de_porciones / 8)

#3