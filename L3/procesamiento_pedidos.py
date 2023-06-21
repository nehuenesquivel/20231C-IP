from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

def procesamiento_pedidos(pedidos: Queue, stock_productos: Dict[str, int], precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  resultado = []
  
  while not pedidos.empty():
    pedido = pedidos.get()
    productos = pedido["productos"]
    precio_total = 0
    cantidad_inicial = {}
    
    for nombre, cantidad in productos.items():
      cantidad_inicial[nombre] = productos[nombre]
      if stock_productos[nombre] - cantidad < 0:
        cantidad_disponible = stock_productos[nombre]
        productos[nombre] = cantidad_disponible
      else:
        cantidad_disponible = cantidad
      stock_productos[nombre] -= cantidad_disponible
      precio_total += precios_productos[nombre] * cantidad_disponible
    pedido["precio_total"] = precio_total
        
    pedido["estado"] = "completo"
    for nombre, cantidad in productos.items():
      if cantidad < cantidad_inicial[nombre]:
        pedido["estado"] = "incompleto"
        break
    
    resultado.append(pedido)

  return resultado

if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))