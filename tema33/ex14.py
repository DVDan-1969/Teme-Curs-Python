
"""Sortează DataFrame-ul după coloana Vârstă descrescător"""
import pandas as pd

df = pd.read_csv('studenti.csv')
print("Date inițiale:")
print(df.head())

df_sortat = df.sort_values(by='Vârstă', ascending=False)
print("\nDate sortate descrescător după vârstă:")
print(df_sortat)