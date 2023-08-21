import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime


api_key = 'AP01EA98BLVTMY5D'
ts = TimeSeries(key=api_key, output_format='pandas')

def extraer_valor(accion):
  data, meta_data = ts.get_daily(symbol=accion, outputsize='compact')
  ultima_fila = data['4. close']
  close = float(ultima_fila[0])
  hora_consulta = datetime.now().strftime('%H:%M:%S')  # Obtiene la hora en formato hh:mm:ss
  return close,hora_consulta

def calcula_variacion (precio_compra,precio_tiempo_real):
  variacion = ((precio_tiempo_real-precio_compra)/precio_compra)*100
  return round(variacion,3)