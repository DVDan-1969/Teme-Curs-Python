"""7. Generează un vector de 10 elemente între 0 și 50. Afișează doar elementele mai mari decât 25."""
import numpy as np

vector = np.random.randint(0, 51, size=10)
print("Vectorul generat:", vector)
elemente_mai_mari = vector[vector > 25]
print("Elementele mai mari decât 25:", elemente_mai_mari)