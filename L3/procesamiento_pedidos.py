from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

def estado_incompleto(pedido: dict[str, Union[int, str, dict[str, int]]]):
  if pedido["estado"] == "completo":
    pedido["estado"] = "incompleto"

def procesamiento_pedidos(pedidos: Queue, stock_productos: Dict[str, int], precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  resultado: list[dict[str, Union[int, str, dict[str, int]]]] = []
  pedido: dict[str, Union[int, str, dict[str, int]]] = {}
  nombre_producto: str = ""
  cantidad_producto: int = 0
  cantidad_disponible: int = 0

  while not pedidos.empty():
    pedido = pedidos.get()
    pedido["precio_total"] = 0
    pedido["estado"] = "completo"

    for producto in pedido["productos"].items():
      nombre_producto = producto[0]
      cantidad_producto = producto[1]

      if stock_productos[nombre_producto] > 0:

        if stock_productos[nombre_producto] - cantidad_producto < 0:
          cantidad_disponible = stock_productos[nombre_producto]
          estado_incompleto(pedido)

        else:
          cantidad_disponible = cantidad_producto
          
        stock_productos[nombre_producto] -= cantidad_disponible
        pedido["productos"][nombre_producto] = cantidad_disponible        
        pedido["precio_total"] += float(precios_productos[nombre_producto] * cantidad_disponible)

      else:        
        pedido["productos"][nombre_producto] = 0
        estado_incompleto(pedido)
    
    resultado.append(pedido)

  return resultado

if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

pedidos: Queue = Queue()
lista_pedidos = json.loads(input())
[pedidos.put(p) for p in lista_pedidos]
stock_productos = json.loads(input())
precios_productos = json.loads(input())
print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))