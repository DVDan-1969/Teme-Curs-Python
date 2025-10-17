
import pandas as pd


df = pd.read_csv('studenti.csv')
studenti_peste_22 = df[df['Vârstă'] > 22]
rezultat = studenti_peste_22[['Nume', 'Vârstă']]
print(rezultat)
