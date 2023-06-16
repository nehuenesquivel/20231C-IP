from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,str]]) -> Dict[str,List[str]]:
  resultado: dict[str, List[str]] = {}
  for diccionario in a_unir:
    for item in diccionario.items():
      if item[0] in resultado:
        resultado[item[0]].append(item[1])
      else:
        resultado[item[0]] = [item[1]]
  return resultado

if __name__ == '__main__':
  x = json.loads(input())
  print(unir_diccionarios(x))