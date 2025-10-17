"""8. Creează un array cu 12 valori de la 1 la 12, transformă-l într-o matrice 3x4, apoi afișează
transpusa acesteia."""

import numpy as np

array = np.arange(1, 13)
print("Array inițial:\n", array)
matrice = array.reshape(3, 4)
print("\nMatricea 3x4:\n", matrice)
transpusa = matrice.T
print("\nTranspusa matricei:\n", transpusa)
