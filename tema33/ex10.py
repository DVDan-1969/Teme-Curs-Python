
import pandas as pd

date_studenti = {
    'Nume': ['Ana Pop', 'Ion Ionescu', 'Maria Radu', 'Dan Georgescu', 'Elena Pavel'],
    'Vârstă': [20, 22, 21, 23, 20],
    'Facultate': ['Informatica', 'Matematică', 'Fizică', 'Biologie', 'Informatica'],
    'An': [2, 3, 1, 4, 2]
}
df = pd.DataFrame(date_studenti)
df.to_csv('studenti.csv', index=False)#evita salvarea indexului in fisierul csv.
print("Fișierul studenti.csv a fost creat cu succes!")
df = pd.read_csv('studenti.csv')
print(df.head())
