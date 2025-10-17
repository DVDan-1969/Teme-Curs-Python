"""13. Adaugă o coloană nouă Nota cu valori între 6 și 10 pentru fiecare student."""

import pandas as pd
import numpy as np

df = pd.read_csv('studenti.csv')
# Generăm valori întregi aleatorii între 6 și 10 pentru fiecare student
df['Nota'] = np.random.randint(6, 11, size=len(df))  # 11 pentru că limita superioară e exclusivă
print(df)
