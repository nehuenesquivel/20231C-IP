from queue import LifoQueue

def calcular_expresion(expr: str) -> float:
    pila: LifoQueue = LifoQueue()
    operaciones: list[str] = ["*", "+", "/", "-"]
    reverso: str = ""
    for elemento in expr.split(" "):
        if elemento in operaciones:
          reverso = pila.get()
          pila.put("(" + pila.get() + elemento + reverso + ")") #pila.put("(" + pila.get() + " " + element + " " + reverso + ")")
        else:
          pila.put(elemento)
    #expresion : str = pila.get()
    #print(expresion)
    return float(eval(pila.get())) #return float(eval(expresion))

if __name__ == '__main__':
  x = input()
  print(round(calcular_expresion(x), 5))