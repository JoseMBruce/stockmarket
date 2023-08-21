import funciones as f

def main():
    
    acciones = [
    {'Nombre': 'AMZN', 'Precio de Compra': 2800.6, 'Cantidad Acciones': 100},
    {'Nombre': 'AAPL', 'Precio de Compra': 170.2, 'Cantidad Acciones': 50},
    {'Nombre': 'MSFT', 'Precio de Compra': 290.85, 'Cantidad Acciones': 70},
    {'Nombre': 'TSLA', 'Precio de Compra': 980.1, 'Cantidad Acciones': 200},
    {'Nombre': 'WMT', 'Precio de Compra': 160.9, 'Cantidad Acciones': 500}
    ]
    
    df = f.pd.DataFrame(acciones)   
    df['Valor en tiempo real'] = float('nan')
    df['Porcentaje de Variación'] = float('nan') 
    df['Hora de consulta'] = None 

    # Llamar a la función para agregar el valor en tiempo real, variacion y hora de consulta
    for index, row in df.iterrows():
        valor_en_tiempo_real, hora_consulta = f.extraer_valor(row['Nombre'])
        df.at[index, 'Valor en tiempo real'] = valor_en_tiempo_real
        df.at[index, 'Porcentaje de Variación'] = f.calcula_variacion(row['Precio de Compra'],valor_en_tiempo_real)
        df.at[index, 'Hora de consulta'] = hora_consulta

    print(df)

if __name__ == "__main__":
    main()