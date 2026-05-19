# ==========================================================
# PROGRAMA: AUDITORÍA DE INVENTARIO
# ==========================================================


# Función para calcular cantidad a solicitar
def calcularPedido(stockActual, stockMinimo):

    if stockActual < stockMinimo:
        return stockMinimo - stockActual
    else:
        return 0


# ==========================================================
# MATRIZ CON DATOS FIJOS
# [Código, Nombre, Stock Actual]
# ==========================================================

inventario = [

    ["A001", "Cuadernos", 15],
    ["A002", "Lapiceros", 50],
    ["A003", "Borradores", 8],
    ["A004", "Reglas", 30],
    ["A005", "Marcadores", 10]

]


print("\n====================================")
print(" SISTEMA DE AUDITORÍA INVENTARIO")
print("====================================")


# ==========================================================
# PEDIR SOLO EL STOCK MÍNIMO
# ==========================================================

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stockActual = articulo[2]

    print("\nCódigo:", codigo)
    print("Nombre:", nombre)
    print("Stock actual:", stockActual)

    stockMinimo = int(
        input("Ingrese stock mínimo: ")
    )

    cantidadPedido = calcularPedido(
        stockActual,
        stockMinimo
    )

    print("Cantidad a pedir:", cantidadPedido)

    print("--------------------------------")


print("\nProceso finalizado")