from typing import List

def mesetaMasLarga(l: List[int]) -> int :
  longitudMeseta: int = 0
  longitudLista: int = len(l)
  if longitudLista < 2:
    longitudMeseta = longitudLista
  else:
    longitud: int = 2
    for i in range(2, longitudLista):
        while(l[i] == l[i - 1]):
          longitud += 1
          i += 1
        longitudMeseta = max(longitudMeseta, longitud) 


      # if (l[i] != l[i - 1] or i + 1 == longitudLista):
      #   longitudMeseta = max(longitudMeseta, i + 1 - inicio)
      #   inicio = i + 1

    # if (l[i] != l[i + 1] or i == len(l) - 2):
    #   longitud = i + 1 - inicio
    #   inicio = i + 1
  return longitudMeseta
if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))