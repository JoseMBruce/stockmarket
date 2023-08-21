"""
    for i in range (len(acciones)):
        dinero_invertido =(dinero_invertido + (precios_compra[i]*cant_acciones[i]))


    mi_rentabilidad = f.rentabilidad(dinero_invertido+ganancia_total, dinero_invertido)

    print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print(f'En resumen:\nTu dinero invertido es: ${dinero_invertido} CLP.\nAhora tienes: ${dinero_invertido+ganancia_total} CLP.\nTu ganancia total es de: ${round(ganancia_total, 2)} CLP.')
    print(f'Tu rentabilidad es de un {round(mi_rentabilidad, 3)}% .\n')
"""

"""
def rentabilidad(beneficio,inversion):
  rentabilidad = ((beneficio-inversion)/inversion)*100
  return rentabilidad
"""

"""

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

"""


""""
close_data = data['4. close']
percentage_change = close_data.pct_change()
print(percentage_change)

last_change = percentage_change[-1]
"""
#if abs(last_change) > 0.0004:
  #  aux= str(last_change)
   # print('MSFT Alert:'+ aux)