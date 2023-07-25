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
