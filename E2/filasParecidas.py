from typing import List

def filasParecidas(matriz: List[List[int]]) -> bool:
  if len(matriz) > 1:
    n: int = matriz[1][0] - matriz[0][0]
    for i in range(1, len(matriz)):
      for j in range(0, len(matriz[i])):
        if matriz[i][j] - matriz[i - 1][j] != n:
          return False
  return True

if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))