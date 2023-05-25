import sys

def fibonacciNoRecursivo(n: int) -> int:
  resultado: int = 0
  if n < 2:
    resultado = n
  else:
    fibonacciN2: int = 0
    fibonacciN1: int = 1
    for i in range(2, n + 1):
      resultado = fibonacciN1 + fibonacciN2
      fibonacciN2 = fibonacciN1
      fibonacciN1 = resultado
  return resultado

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))