from typing import List
from typing import Tuple

#implementación inficiente:
# 1. si en los vuelos no está el origen y el destino, itera los vuelos en vano
# 2. si en los vuelos está el origen y el destino, itera los vuelos intermedios más de una vez
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int:
  resultado: int = 0
  longitud: int = len(vuelos)
  escala: str = origen
  i: int = 0
  while escala != destino and i < longitud:
    for j in range(0, longitud):
      if vuelos[j][0] == escala:
        escala = vuelos[j][1]
        resultado += 1
    i += 1
  return resultado if escala == destino else -1

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))