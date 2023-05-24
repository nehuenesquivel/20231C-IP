import sys

def fibonacciNoRecursivo(n: int) -> int:
  fibonacciN: int = 0
  if n < 2:
    fibonacciN = n
  else:
    fibonacciN2: int = 0
    fibonacciN1: int = 1
    for i in range(2, n + 1):
      fibonacciN = fibonacciN1 + fibonacciN2
      fibonacciN2 = fibonacciN1
      fibonacciN1 = fibonacciN
  return fibonacciN

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))