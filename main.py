import funciones as f

def main():
    
    acciones = [
    {'nombre': 'AMZN', 'precio_compra': 2800.6, 'cant_acciones': 100},
    {'nombre': 'AAPL', 'precio_compra': 170.2, 'cant_acciones': 50},
    {'nombre': 'MSFT', 'precio_compra': 290.85, 'cant_acciones': 70},
    {'nombre': 'TSLA', 'precio_compra': 980.1, 'cant_acciones': 200},
    {'nombre': 'WMT', 'precio_compra': 160.9, 'cant_acciones': 500}
]

    f.calcular_ganancias(acciones)

    
"""
    for i in range (len(acciones)):
        dinero_invertido =(dinero_invertido + (precios_compra[i]*cant_acciones[i]))


    mi_rentabilidad = f.rentabilidad(dinero_invertido+ganancia_total, dinero_invertido)

    print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print(f'En resumen:\nTu dinero invertido es: ${dinero_invertido} CLP.\nAhora tienes: ${dinero_invertido+ganancia_total} CLP.\nTu ganancia total es de: ${round(ganancia_total, 2)} CLP.')
    print(f'Tu rentabilidad es de un {round(mi_rentabilidad, 3)}% .\n')

"""

if __name__ == "__main__":
    main()


""""
close_data = data['4. close']
percentage_change = close_data.pct_change()
print(percentage_change)

last_change = percentage_change[-1]
"""
#if abs(last_change) > 0.0004:
  #  aux= str(last_change)
   # print('MSFT Alert:'+ aux)

   