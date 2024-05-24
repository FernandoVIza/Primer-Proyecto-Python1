# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:29:02 2024

@author: fernandovz
"""

import numpy as np

# 01: Crear un array 7x8 lleno de ceros de tipo entero
array_ceros = np.zeros((7, 8), dtype=int)
print("Array 7x8 lleno de ceros de tipo entero:")
print(array_ceros)

# 02: Crear un array 7x8 lleno de ceros salvo la primera fila que serán todo unos
array_ceros_primera_fila_unos = np.zeros((7, 8), dtype=int)
array_ceros_primera_fila_unos[0, :] = 1
print("\nArray 7x8 lleno de ceros salvo la primera fila que serán todo unos:")
print(array_ceros_primera_fila_unos)

# 03: Crear un array 7x8 lleno de ceros salvo la última fila que será el rango entre 5 y 12
array_ceros_ultima_fila_rango = np.zeros((7, 8), dtype=int)
array_ceros_ultima_fila_rango[-1, :] = np.arange(5, 13)
print("\nArray 7x8 lleno de ceros salvo la última fila que será el rango entre 5 y 12:")
print(array_ceros_ultima_fila_rango)
