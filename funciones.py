import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'AP01EA98BLVTMY5D'
ts = TimeSeries(key=api_key, output_format='pandas')

def extraer_valor(accion):
  data, meta_data = ts.get_daily(symbol=accion, outputsize='compact')
  ultima_fila = data['4. close']
  close = float(ultima_fila[0])
  return close

def rentabilidad(beneficio,inversion):
  rentabilidad = ((beneficio-inversion)/inversion)*100
  return rentabilidad


def calcular_ganancias(acciones):
    ganancia_total = 0

    for accion in acciones:
        nombre = accion['nombre']
        precio_compra = accion['precio_compra']
        cant_acciones = accion['cant_acciones']
    
        valor_actual = extraer_valor(nombre)
        ganancia = round((valor_actual - precio_compra) * cant_acciones, 2) 
        print(f'El valor de la acción {nombre} es de ${valor_actual} y tu compraste en ${precio_compra}, por lo que tu ganancia es de: ${ganancia}')
    
        ganancia_total += ganancia

    print(f'La ganancia total es de: ${ganancia_total}')
