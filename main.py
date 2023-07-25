import funciones as f

def main():
    
    acciones = ['AMZN','AAPL','MSFT','TSLA','WMT']
    precios_compra = [2800.6, 170.2,290.85, 980.1, 160.9]
    cant_acciones = [100,50,70,200,500]
    count = 0
    ganancia_total = 0
    dinero_invertido = 0

    print('\n')
    for i in acciones:
        valor_actual = f.extraer_valor(i)
        ganancia = round( ((valor_actual - (precios_compra[count]))*cant_acciones[count]) , 2) 
        print(f'El valor de la acción {i} es de ${valor_actual} y tu compraste en ${precios_compra[count]}, por lo que tu ganancia es de: ${ganancia}')
        ganancia_total = ganancia_total + ganancia
        count = count + 1



    for i in range (len(acciones)):
        dinero_invertido =(dinero_invertido + (precios_compra[i]*cant_acciones[i]))


    mi_rentabilidad = f.rentabilidad(dinero_invertido+ganancia_total, dinero_invertido)

    print("------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print(f'En resumen:\nTu dinero invertido es: ${dinero_invertido} CLP.\nAhora tienes: ${dinero_invertido+ganancia_total} CLP.\nTu ganancia total es de: ${round(ganancia_total, 2)} CLP.')
    print(f'Tu rentabilidad es de un {round(mi_rentabilidad, 3)}% .\n')



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

   