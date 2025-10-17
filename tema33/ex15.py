"""Grupează studenții după Oraș și calculează media notelor pentru fiecare oraș."""

import pandas as pd


date_studenti = {
    'Nume': ['Ana Pop', 'Ion Ionescu', 'Maria Radu', 'Dan Georgescu', 'Elena Pavel'],
    'Vârstă': [20, 22, 21, 23, 20],
    'Facultate': ['Informatica', 'Matematică', 'Fizică', 'Biologie', 'Informatica'],
    'An': [2, 3, 1, 4, 2],
    'Oraș': ['Cluj', 'București', 'Cluj', 'Iași', 'București'],
    'Nota': [9.5, 8.0, 9.0, 7.5, 8.5]
}

df = pd.DataFrame(date_studenti)
medii_pe_oras = df.groupby('Oraș')['Nota'].mean()# Gruparea după oraș și calculul mediei notelor
print("Media notelor pe fiecare oraș:")
print(medii_pe_oras)

"""16. Salvează DataFrame-ul final într-un fișier studenti_procesati.csv fără index."""
medii_pe_oras = df.groupby('Oraș')['Nota'].mean().reset_index()
medii_pe_oras.to_csv('studenti_procesati.csv', index=False)
