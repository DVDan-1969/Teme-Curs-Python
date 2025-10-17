"""Creează un vector NumPy care conține numerele de la 0 la 9 și afișează doar elementele pare."""
import numpy as np

# Crearea vectorului cu numerele de la 0 la 9
vector = np.arange(10)
elemente_pare = vector[vector % 2 == 0]
print(elemente_pare)