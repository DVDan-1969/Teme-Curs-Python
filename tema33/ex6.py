"""6. * Generează o matrice 4x4 cu numere întregi aleatoare între 0 și 20. Afișează valoarea maximă,
minimă și poziția lor (index)."""

import numpy as np

matrice = np.random.randint(0, 21, size=(4, 4))
print("Matricea generată:\n", matrice)
valoarea_maxima = np.max(matrice)
print("Valoare maxima:\n", valoarea_maxima)
valoare_minima = np.min(matrice)
print("Valoare minima:\n", valoare_minima)

pozitie_max = tuple(int(i) for i in np.unravel_index(np.argmax(matrice), matrice.shape))
print("Poziția valorii maxime (linie, coloană):", pozitie_max)

pozitie_min = tuple(int(i) for i in np.unravel_index(np.argmin(matrice), matrice.shape))
print("Poziția valorii minime (linie, coloană):", pozitie_min)