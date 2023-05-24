#1
def pertenece(s: list, e: int) -> bool:
    for i in range(0, len(s)):
        if s[i] == e:
            return True
    return False

def divideATodos(s: list, e: int) -> bool:
    for i in range(0, len(s)):
        if s[i] % e != 0:
            return False
    return True

def sumaTotal(s: list[int]) -> int:
    resultado: int = 0
    for i in range(0, len(s)):
        resultado += s[i]
    return resultado

def ordenados(s: list) -> bool:
    for i in range(0, len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

def palabra_con_longitud_mayor_a_siete(s: list) -> bool:
    for i in range(0, len(s)):
        if len(s[i]) > 7:
            return True
    return False

def palabra_palindroma(s: str) -> bool:
    return str == str[::-1]

def fortaleza_de_contraseña(s: str) -> str:
    longitud: int = len(str)
    if longitud < 5:
        return "ROJA"
    elif longitud > 8 and incluido(str, ("a", "z")) and incluido(str, ("A", "Z")) and incluido(str, (0, 9)):
        return "VERDE"
    else:
        return "AMARILLA"

def incluido(s: str, l: tuple) -> bool:
    for i in range(0, len(s)):
        if l[0] <= s[i] <= l[1]:
            return True
    return False