from queue import Queue

def avanzarFila(fila: Queue, min: int):
  nueva_persona = fila.qsize() + 1
  persona_problematica = 0

  for minuto in range(0, min + 1):

    #final de la fila
    if persona_problematica != 0 and (minuto - 3) % 4 == 2:
      # print(str(minuto) + "persona problematica")
      fila.put(persona_problematica)
      persona_problematica = 0      
      
    #nueva persona
    if minuto % 4 == 0:
      # print(str(minuto) + "nueva persona")
      fila.put(nueva_persona)
      nueva_persona += 1
      
    #caja1
    if minuto % 10 == 1:
      # print(str(minuto) + "caja1")
      if not fila.empty():
        fila.get()

    #caja2
    if minuto % 4 == 3:
      # print(str(minuto) + "caja2")
      if not fila.empty():
        fila.get()
    
    #caja3
    if minuto % 4 == 2:
      # print(str(minuto) + "caja3")
      if not fila.empty():
        persona_problematica = fila.get()

  return fila

# q = Queue()
# for e in [1, 2, 3]:
#   q.put(e)
# avanzarFila(q, 4)
# l = []
# while not q.empty():
#   l.append(q.get())
# print(l)

if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)