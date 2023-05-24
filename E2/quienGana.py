import sys

def papelGanaAPiedra(j1: str, j2: str) -> bool:
  return j1 == "Papel" and j2 == "Piedra"

def tijeraGanaAPapel(j1: str, j2: str) -> bool:
  return j1 == "Tijera" and j2 == "Papel"

def piedraGanaATijera(j1: str, j2: str) -> bool:
  return j1 == "Piedra" and j2 == "Tijera"

def gana(j1: str, j2: str) -> bool:
  return piedraGanaATijera(j1, j2) or tijeraGanaAPapel(j1, j2) or papelGanaAPiedra(j1, j2)

def quienGana(j1: str, j2: str) -> str: 
  if gana(j1, j2):
    return "Jugador1"
  elif gana(j2, j1):
    return "Jugador2"
  else:
    return "Empate"

if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))