'''1.Se dau listele:
angajati = ['Maria', 'Marius', 'Andrei', 'Bianca', 'Bogdan', 'Ana', 'Mihai']
card_combustibil = ['Maria', 'Andrei']
abonament_sala = ['Maria', 'Andrei', 'Mihai']

Care sunt angajatii care au si card de combustibil si abonament la sala?
Care sunt angajatii care nu au nici card de combustibil si nici abonament la sala?

2.	Eliminati duplicatele din cadrul unui cuvant introdus de la trastatura.

3.	Jocul 6/49 folosind set-uri.

4.	Se citeste un numar intreg, de 4 cifre, de la tastatura. Afisati care este urmatorul
numar de 4 cifre, cu toate cifrele distincte, folosind set-uri.
Ex: 1003 -> 1023

5.	Afisati care sunt consoanele dintr-un string introdus de la tastatura folosind seturi.

6.	Se dau doua liste. Afisati care sunt elementele comune celor 2 liste. Afisati si
 elementele diferite.

7.	* Se da un string. Verificati daca printr-o singura eliminare a unui caracter din
 string, frecventa de aparitie a caracterelor va fi aceeasi pentru fiecare caracter, sau
  pentru caracterele ramase.
ex:
s = ‘pptthhh’
Se poate → se elimina h si frecventa va fi 2 2 2

s = ‘xyyyzzz’
Se poate → se elimina x si frecventa va fi 3 3

s = ‘ppttthhh’
Nu se poate → nu putem face nicio eliminare a unui caracter din string astfel incat
frecventa de aparitie a caracterelor sa fie aceeasi.'''
#2
# cuvant = input("Introdu un cuvânt: ")
# rezultat = ""
# for char in cuvant:
#     if char not in rezultat:
#         rezultat +=char
# print("Cuvântul fără duplicate:", rezultat)
#3
import random

# def joc_6_din_49():
#     numere_extrase = set(random.sample(range(1, 50), 6))  # generam 6 numere
#     print("Numerele extrase la 6/49 sunt:", sorted(numere_extrase))
# joc_6_din_49()
#4
# numar = int(input("Introduceți un număr de 4 cifre: "))
# numar += 1
# while numar <= 9999:
#     if len(set(str(numar))) == 4:
#         print("Următorul număr cu toate cifrele distincte este:", numar)
#         break
#     numar += 1

#5
# str=input("Itroduceti sirul de la tastatura:")
# set1={"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v",
#       "x","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","X","Z"}
# set2=set(str)
# set=set1&set2
# print(set)
#6
# input_string = input("Introdu o listă de numere, separate prin virgulă: ")
# lista1 = [int(x) for x in input_string.split(',')]
# print(lista1)
# input_string = input("Introdu o listă de cuvinte, separate prin spațiu: ")
# lista2 = input_string.split()
# print(lista2)
# set1 = set(lista1)
# print(set1)
# set2 = set(lista2)
# print(set2)
# comune = set1 & set2
# print(comune)
# diferente1 = set1 - set2
# print(diferente1)
# diferente2 = set2 - set1
# print(diferente2)
'''List and dictionary comprehension'''
'''
1.	Afiseaza o lista cu toate patratele perfecte intre 0 si 100 folosind list comprehension                                 

2.	Se da lista numbers = [50, 9, 100, 3, 33, ‘22’]
Transforma intregii in string-uri folosind list comprehension

3.	Se da dictionarul de mai jos cu pretul masinilor in EUR

	cars = {
    'Dacia': 15000,
    'Toyota': 20000,
    'BMW': 50000,
    'Audi': 45000,
    'Hyundai': 16500,
    'Mercedes': 70000
}

Afisati un dictionar cu pretul masinilor in RON folosind dictionary comprehension
Creati un dictionar cu toate masinile mai scumpe de 20k EUR folosind dictionary comprehension

4.	Afisati de cate ori apare fiecare caracter dintr-un cuvant folosind dictionary comprehension

5.	Se da o lista.
Afisati o lista care contine elementele True si False; True daca elementul din lista 
initiala este string si false daca elementul nu este string. Implementarea va fi cu 
list comprehension.
	ex:
l = [1, 2, 3, 'Python', 'java']
result = [False, False, False, True, True]

6.	Afisati daca numerele dintr-o lista sunt mai mari decat 10 folositi 
dictionary comprehension.
ex:
numbers = [1, 2, 3, 100, 200, 300]
result = {1: False, 2: False, 3: False, 100: True, 200: True, 300: True}
'''
#1
# patrate_perfecte = [x**2 for x in range(11) if x**2 <= 100]
# print(patrate_perfecte)

#2
# numere = [50, 9, 100, 3, 33, '22']
# numere_ca_siruri = [str(x) for x in numere]
# print(numere_ca_siruri)
# #3
# cars = {
#     'Dacia': 15000,
#     'Toyota': 20000,
#     'BMW': 50000,
#     'Audi': 45000,
#     'Hyundai': 16500,
#     'Mercedes': 70000
# }
# eur_to_ron = 5
# cars_ron = {car: price * eur_to_ron for car, price in cars.items()}
# print(cars_ron)
# expensive_cars = {car: price for car, price in cars.items() if price > 20000}
# print(expensive_cars)
# #4
# str=input("Itroduceti cuvantul de la tastatura:")
# char_count = {char: str.count(char) for char in str}
# print(char_count)
#5
# str1 = input("Introduceți elementele, separate prin spațiu: ")
# lista_input = str1.split()
# lista_mixta = []
# for element in lista_input:
#     try:
#         # Încearcă să convertească la int
#         numar = int(element)
#         lista_mixta.append(numar)
#     except ValueError:
#         # Dacă nu poate, păstrează ca string
#         lista_mixta.append(element)
# print(lista_mixta)
# rezultat = [isinstance(element, str) for element in lista_mixta]
# print(rezultat)
#6
# lista_numere = [5, 12, 7, 20, 3, 15]
# dictionar = {numar: (numar > 10) for numar in lista_numere}
# print(dictionar)
