# ==========================================
# PROBLEMA 3 - AUDITORÍA DE INVENTARIO
# ==========================================

# Función para calcular la cantidad exacta a pedir
def calcularPedido(stockActual, stockMinimo):

    if stockActual < stockMinimo:
        return stockMinimo - stockActual
    else:
        return 0


# Matriz de artículos
# [Código, Nombre, Stock Actual, Stock Mínimo]

inventario = [

    ["A001", "Cuadernos", 15, 20],
    ["A002", "Lapiceros", 50, 40],
    ["A003", "Borradores", 8, 15],
    ["A004", "Reglas", 30, 25],
    ["A005", "Marcadores", 10, 20]

]


print("\n===== LISTA DE PEDIDOS =====\n")

# Recorrer la matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stockActual = articulo[2]
    stockMinimo = articulo[3]

    # Llamado a la función
    cantidadPedido = calcularPedido(
        stockActual,
        stockMinimo
    )

    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock actual:", stockActual)
    print("Stock mínimo:", stockMinimo)
    print("Cantidad a pedir:", cantidadPedido)

    print("----------------------------")