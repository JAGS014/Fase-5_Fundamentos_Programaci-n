# Jorge Armando Gonzalez Salamanca
# Grupo: 213022_492
# Programa: Ingeniería de Sistemas
# Codigo fuente: autoría propia 

productos = [
                  [1, "Cuaderno", 30, 30],
                  [2, "Esfero", 15, 50],
                  [3, "Lapiz", 10, 50],
                  [4, "Resaltador", 18, 20],
                  [5, "Sacapuntas", 13, 30]
]
def calculo_reabastecimiento(stock_actual, stock_minimo):
     if stock_actual < stock_minimo:
        cantidad_reabastecer = stock_minimo - stock_actual
        return cantidad_reabastecer
     else:
            return 0
for producto in productos:
    codigo = producto[0]
    nombre = producto[1]
    stock_actual = producto[2]
    stock_minimo = producto[3]
    cantidad_reabastecer = calculo_reabastecimiento(stock_actual, stock_minimo)
    if cantidad_reabastecer > 0:
        print(f"Producto: {nombre} (Código: {codigo}) - Reabastecer: {cantidad_reabastecer} unidades")
    else:
        print(f"Producto: {nombre} (Código: {codigo}) - No requiere reabastecimiento")

