
import pandas as pd

df = pd.read_csv('studenti.csv')
print("Dimensiunea DataFrame-ului (shape):", df.shape)
print("\nTipurile de date (dtypes):")
print(df.dtypes)
print("\nValori lipsă în fiecare coloană (isnull().sum()):")
print(df.isnull().sum())
