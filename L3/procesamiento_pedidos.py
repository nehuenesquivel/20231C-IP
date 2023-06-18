from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

def procesamiento_pedidos(pedidos: Queue, stock_productos: Dict[str, int], precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  resultado = []
  pedido = {}
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
          if pedido["estado"] == "completo":
            pedido["estado"] = "incompleto"

        else:
          cantidad_disponible = cantidad_producto
          
        stock_productos[nombre_producto] -= cantidad_disponible
        pedido["productos"][nombre_producto] = cantidad_disponible        
        pedido["precio_total"] += float(precios_productos[nombre_producto] * cantidad_disponible)

      else:        
        pedido["productos"][nombre_producto] = 0
        if pedido["estado"] == "completo":
          pedido["estado"] = "incompleto"
    
    resultado.append(pedido)

  return resultado

if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))