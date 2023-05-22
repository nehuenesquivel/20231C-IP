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
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 or numero2 == 0

def ambos_son_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 and numero2 == 0

def es_nombre_largo(nombre: str) -> bool:
    return 2 < len(nombre) < 9

def es_bisiesto(ano: int) -> bool:
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

#4
def peso_pino(altura: float) -> float:
    return altura * 300 if altura <= 3 else 900 + (altura - 3) * 200

def es_peso_util(peso: float) -> bool:
    return 400 <= peso <= 1000

def sirve_pino(altura: float) -> bool:
    return es_peso_util(peso_pino(altura))

#6
def imprimir_numeros_del_1_al_10_a():
    i: int = 1
    while i < 11:
        print(i)
        i += 1

def imprimir_numeros_pares_del_10_al_40_a():
    i: int = 10
    while i < 41:
        if i % 2 == 0:
            print(i)
        i += 1

def imprimir_palabra_eco_10_veces_a():
    i: int = 1
    while i < 11:
        print("eco")
        i += 1

def imprimir_cuenta_regresiva_a(numero: int):
    i: int = numero
    while i > 0:
        print(i)
        i -= 1
    print("despegue")

def imprimir_viaje_en_el_tiempo_a(año_de_partida: int, año_de_llegada: int):
    i: int = año_de_partida
    while i > año_de_llegada:
        i -= 1
        print("viajó un año al pasado, estamos en el año: " + str(i))
        

def imprimir_viaje_en_el_tiempo_hasta_aristoteles_a(año_de_partida: int):
    i: int = año_de_partida - 20
    while i > -385:
        print("viajó veinte años al pasado, estamos en el año: " + str(i))
        i -= 20

#7
def imprimir_numeros_del_1_al_10_b():
    for i in range(1, 11):
        print(i)

def imprimir_numeros_pares_del_10_al_40_b():
    for i in range(10, 41, 2):
        print(i)

def imprimir_palabra_eco_10_veces_b():
    for i in range(1, 11):
        print("eco")

def imprimir_cuenta_regresiva_b(numero: int):
    for i in range(numero, 0, -1):
        print(i)
    print("despegue")

def imprimir_viaje_en_el_tiempo_b(año_de_partida: int, año_de_llegada: int):
    for i in range(año_de_partida - 1, año_de_llegada - 1, -1):
        print("viajó un año al pasado, estamos en el año: " + str(i))

def imprimir_viaje_en_el_tiempo_hasta_aristoteles_b(año_de_partida: int):
    for i in range(año_de_partida -20, -385, -20):
        print("viajó veinte años al pasado, estamos en el año: " + str(i))