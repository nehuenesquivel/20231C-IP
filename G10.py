#1
def contar_lineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo)
    lineas: list[str] = archivo.readlines()
    archivo.close()
    return len(lineas)

def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    resultado: bool = False
    archivo = open(nombre_archivo)
    lineas: list[str] = archivo.readlines()
    for i in range(0, len(lineas)):
        if palabra in lineas[i]:
            resultado = True
            break
    archivo.close()
    return resultado

def cantidad_apariciones(nombre_archivo: str, palabra: str) -> int:
    resultado: int = 0
    archivo = open(nombre_archivo)
    lineas: list[str] = archivo.readlines()
    for i in range(0, len(lineas)):
        resultado += lineas[i].replace("\n", "").split(" ").count(palabra)
    archivo.close()
    return resultado

#8