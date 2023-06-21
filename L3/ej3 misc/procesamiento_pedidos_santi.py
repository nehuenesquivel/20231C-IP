from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:

  res = []

  while not pedidos.empty():

    pedido = pedidos.get()
    cantidades_iniciales = {}

    productos = pedido["productos"]
    precio = 0


    for producto, cantidad in productos.items():

      cantidades_iniciales[producto] = productos[producto]

      if stock_productos[producto] - cantidad >= 0:

        stock_productos[producto] -= cantidad
        precio += precios_productos[producto]*cantidad
        pedido["precio_total"] = precio

      else:

        lleva = stock_productos[producto]
        productos[producto] = lleva
        stock_productos[producto] = 0
        precio += precios_productos[producto]*lleva
        pedido["precio_total"] = precio

    for prod in cantidades_iniciales:
      if cantidades_iniciales[prod] != productos[prod]:
        pedido["estado"] = "incompleto"
        break
      else:
        pedido["estado"] = "completo"



    res.append(pedido)

  return res


if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))