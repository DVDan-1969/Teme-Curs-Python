"""9. Creează un DataFrame cu următoarele coloane: Nume, Vârstă, Oraș, conținând 5 rânduri de
date fictive."""

import pandas as pd

date = {
    'Nume': ['Ana Popescu', 'Mihai Ionescu', 'Elena Georgescu', 'Andrei Vasilescu', 'Ioana Marinescu'],
    'Vârstă': [25, 32, 28, 40, 22],
    'Oraș': ['București', 'Cluj-Napoca', 'Iași', 'Timișoara', 'Brașov']
}
df = pd.DataFrame(date)
print(df)
