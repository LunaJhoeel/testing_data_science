# Importa módulos de Python estándar primero
import os
import sys
import datetime

# Importa módulos de terceros después
import numpy as np
import pandas as pd

# Importa tus propios módulos al final
from mi_modulo_personal import funcion_personal

# Declaración de una constante en mayúsculas con guiones bajos (snake_case)
MI_CONSTANTE = 42
PI = 3.14159

# Declaración de una variable en minúsculas con guiones bajos (snake_case)
nombre_variable = "Precio_unitario"

# Declaración de una lista con espacios en blanco consistentes
mi_lista = [1, 2, 3, 4, 5]

# Declaración de una tupla con espacios en blanco consistentes
mi_tupla = (10, 20, 30, 40, 50)

# Declaración de un diccionario con espacios en blanco consistentes
mi_diccionario = {
    'clave1': 'valor1',
    'clave2': 'valor2',
    'clave3': 'valor3',
}

# Definición de una función con espacios en blanco
def mi_funcion(parametro1, parametro2):
    """
    Esta es una función de ejemplo.
    """
    resultado = parametro1 + parametro2
    return resultado

# Definición de una función en minúsculas con guiones bajos (snake_case)
def calcular_total(precio_unitario, cantidad):
    """
    Esta función calcula el precio total de una compra multiplicando el precio unitario por la cantidad.
    """
    # Calcular el precio total
    precio_total = precio_unitario * cantidad
    
    # Imprimir el resultado
    print(f"El {nombre_variable} es ${precio_unitario} y la cantidad es {cantidad}. El precio total es ${precio_total}.")

# Llamada a la función con un comentario explicativo
precio_unitario = 10
cantidad = 5
calcular_total(precio_unitario, cantidad)  # Calcular y mostrar el precio total

# Manejo de excepciones con comentarios explicativos
try:
    resultado = 10 / 0
except ZeroDivisionError as error:
    # Capturamos la excepción ZeroDivisionError y mostramos un mensaje
    print(f"Error: {error}")

