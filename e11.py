def procesar_inventario():
    productos = ["Monitor", "Teclado", "Mouse"]
    stock = [15, 8, 20]
    precios = [25000, 5000, 3500]
    
    ventas_totales = 0
    pedidos_pendientes = [10, 12, 5] 

    print("--- Sistema de Despacho de Almacén ---")

    for i in range(len(productos)):
        nombre = productos[i]
        cantidad_pedida = pedidos_pendientes[i]
        stock_actual = stock[i]
        precio_unitario = precios[i]

        print(f"Analizando pedido de: {nombre}")

        if stock_actual < cantidad_pedida:
            total_operacion = cantidad_pedida * precio_unitario
            ventas_totales += total_operacion
            stock[i] = stock_actual - cantidad_pedida
            print(f"Pedido procesado. Stock restante: {stock[i]}")
        else:
            print(f"Error: Stock insuficiente para {nombre}. Stock: {stock_actual}")

    print("---------------------------------------")
    print(f"Resumen del día. Ventas totales: ${ventas_totales}")
    print(f"Estado final del stock: {stock}")

procesar_inventario()