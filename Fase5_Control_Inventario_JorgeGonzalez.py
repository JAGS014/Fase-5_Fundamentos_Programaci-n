#----------------------------------
# Jorge Armando Gonzalez Salamanca
# Grupo: 213022_492
# Programa: Ingeniería de Sistemas
# Codigo fuente: autoría propia 
#----------------------------------

# Almacenamos los datos de 5 articulos con la estructura: [codigo, nombre, stock_actual, stock_minimo].
productos = [
                  [1, "Cuaderno", 30, 30],
                  [2, "Esfero", 15, 50],
                  [3, "Lapiz", 10, 50],
                  [4, "Resaltador", 18, 20],
                  [5, "Sacapuntas", 13, 30]
]

# Se recibe el stock actual y el stock mínimo de un producto.
# Si el stock actual es menor que el stock mínimo, se calcula y retorna la cantidad que falta y si no retorna 0.
def calculo_reabastecimiento(stock_actual, stock_minimo):
     if stock_actual < stock_minimo:
        cantidad_reabastecer = stock_minimo - stock_actual
        return cantidad_reabastecer
     else:
            return 0

# Creamos un bucle "for" para recorrer la lista de productos dentro de la matriz 'productos'.     
for producto in productos:
    codigo = producto[0]
    nombre = producto[1]
    stock_actual = producto[2]
    stock_minimo = producto[3]

    # Llamamos a la función 'calculo_reabastecimiento' para `saber` si se necesita reabastecer el producto y la cantidad que se necesita.
    cantidad_reabastecer = calculo_reabastecimiento(stock_actual, stock_minimo)

    # Verificamos el resultado de la función y mostramos un mensaje indicando si se necesita reabastecer el producto o no.
    if cantidad_reabastecer > 0:
        print(f"Producto: {nombre} (Código: {codigo}) - Reabastecer: {cantidad_reabastecer} unidades")
    else:
        print(f"Producto: {nombre} (Código: {codigo}) - No requiere reabastecimiento")

