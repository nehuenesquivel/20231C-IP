from typing import List

def mesetaMasLarga(l: List[int]) -> int :
  longitud: int = len(l)
  resultado: int = 0
  j: int = 0
  for i in range(0, longitud):
    while(i + 1 < longitud and l[i] == l[i + 1]):
      i += 1
    resultado = max(resultado, i - j + 1)
    j = i + 1
  return resultado

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))