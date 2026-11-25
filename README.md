# 📝Desarrollo Fase 5 - Evaluación Final POA: Control de inventario📝
----------------------------------------
## 📌Información del Estudiante
* Estudiante: Jorge Armando Gonzalez Salamanca
* Curso: Fundamentos de Programación (213022)
* Grupo: 213022_492
* Programa: Ingeniería de Sistemas
* Institución: Universidad Nacional Abierta y a Distancia (UNAD)
---------------------------
## 📝Descripción del Problema
Este repositorio contiene la solución desarrollada en Python para el problema 3 de la evaluación fianal POA del curso Fundamentos de Programación de la UNAD.
Este programa administra un inventario almacenado en una matriz bidimensional con 5 productos ([Código, Nombre, Stock Actual, Stock Mínimo]). 
El cual evalúa de forma automática haciendo uso de una función modular si la cantidad en stock de cada artículo está por debajo del mínimo requerido
para determinar las unidades exactas a reabastecer.
------------
```python
# Almacenamos los datos de 5 articulos con la estructura: [codigo, nombre, stock_actual, stock_minimo].
productos = [
    [1, "Cuaderno", 5, 30], 
    [2, "Esfero", 15, 50], 
    [3, "Lapiz", 10, 50], 
    [4, "Resaltador", 18, 20], 
    [5, "Sacapuntas", 13, 30] 
]

# Se recibe el stock actual y el stock mínimo de un producto.
# Si el stock actual es menor que el stock mínimo, se calcula y retorna la cantidad que falta y si no retorna 0.
def calculo_reabastecimiento(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
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
```
