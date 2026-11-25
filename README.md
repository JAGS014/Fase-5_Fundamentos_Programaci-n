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
productos = [
    [1, "Cuaderno", 5, 30], 
    [2, "Esfero", 15, 50], 
    [3, "Lapiz", 10, 50], 
    [4, "Resaltador", 18, 20], 
    [5, "Sacapuntas", 13, 30] 
]
def calculo_reabastecimiento(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
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
```
