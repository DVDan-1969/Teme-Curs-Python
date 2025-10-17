"""4. Creează un array cu valorile de la 0 la 11 și transformă-l într-o matrice 3x4."""

import numpy as np

array = np.arange(12)
print(array)
matrice = array.reshape((3,4))
print(matrice)
