from queue import LifoQueue

def calcular_expresion(expr: str) -> float:
    pila: LifoQueue = LifoQueue()
    operaciones: list[str] = ["*", "+", "/", "-"]
    reverso: str = ""
    for char in expr.split(" "):
        if char in operaciones:
          reverso = pila.get()
          pila.put("(" + pila.get() + " " + char + " " + reverso + ")")
        else:
          pila.put(char)
    expresion : str = pila.get()
    print(expresion)
    return float(eval(expresion)) #return float(eval(pila.get()))

if __name__ == '__main__':
  x = input()
  print(round(calcular_expresion(x), 5))