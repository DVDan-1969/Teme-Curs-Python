'''Dată o listă de șiruri de caractere (toate cu litere mici), folosește map și lambda pentru
a le transforma în litere mari.'''

# lista_mici = ['mere', 'banane', 'cirese']
# lista_mari = list(map(lambda x: x.upper(), lista_mici))
# print(lista_mari)

'''Dată o listă de cuvinte, folosește map și lambda pentru a obține lungimea fiecărui cuvânt.'''

# cuvinte = ["măr", "păr", "banană", "portocală", "kiwi"]
# lungimi = list(map(lambda cuvant: len(cuvant), cuvinte))
# print (lungimi)

'''Date două liste de numere, folosește map și lambda pentru a înmulți elementele corespunzătoare dintre 
cele două liste (din [2, 4, 6] si [3, 5, 7] obtinem [6, 20, 42]).'''

# lista1 = [2, 4, 6]
# lista2 = [3, 5, 7]
# produs = list(map(lambda x, y: x * y, lista1, lista2))
# print(produs)
'''Date două liste, una cu prenume și alta cu nume de familie, folosește map și lambda pentru a le combina 
într-o listă de nume complete (din ["Ion", "Maria", "Andrei"] si ["Popescu", "Ionescu", "Georgescu"] obtinem 
["Ion Popescu", "Maria Ionescu", "Andrei Georgescu"]).'''

# prenume = ["Ion", "Maria", "Andrei"]
# nume_familie = ["Popescu", "Ionescu", "Georgescu"]
# nume_complete = list(map(lambda p, n: p + " " + n, prenume, nume_familie))
# print(nume_complete)

'''Creează un decorator care afișează un mesaj înainte și după apelarea unei funcții'''
# def decorator_mesaj(func):
#     def wrapper(*args, **kwargs):
#         print("Înainte de apelarea funcției.")
#         result = func(*args, **kwargs)
#         print("După apelarea funcției.")
#         return result
#     return wrapper
#
# @decorator_mesaj
# def salut():
#     print("Salut, lume!")
# salut()
'''Creează un decorator care apelează funcția decorată de 3 ori.'''

# def de_trei_ori(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             print(f"Apelul {i+1}:")
#             func(*args, **kwargs)
#     return wrapper

# @de_trei_ori
# def salut():
#     print("Salut, lume!")
# salut()
'''Creează un decorator care verifică dacă toate argumentele unei funcții sunt de tip int. 
Dacă nu, afișează un mesaj de eroare și nu apelează funcția.'''

# def only_ints(func):
#     def wrapper(*args, **kwargs):
#         # Verificăm argumentele poziționale
#         for arg in args:
#             if not isinstance(arg, int):
#                 print(f"Eroare: Argumentul {arg} nu este de tip int.")
#                 return

        # Verificăm argumentele numite (kwargs)
#         for key, value in kwargs.items():
#             if not isinstance(value, int):
#                 print(f"Eroare: Argumentul '{key}' cu valoarea {value} nu este de tip int.")
#                 return
#
#         # Dacă toate argumentele sunt int, apelăm funcția
#         return func(*args, **kwargs)
#     return wrapper
#
# @only_ints
# def aduna(a, b):
#     return a + b

# Exemplu de utilizare
# rezultat = aduna(3, 5)
# if rezultat is not None:
#     print(f"Suma este: {rezultat}")
# aduna(a=10, b="20")
'''Fă un generator care primește un șir de caractere și le returnează unul câte unul'''

# def generator_caractere(sir):
#     for caracter in sir:
#         yield caracter
#
# sir = "Salut"
# gen = generator_caractere(sir)
#
# for caracter in gen:
#     print(caracter)
'''Creează un generator care produce primii n termeni din șirul lui Fibonacci'''

# def fibonacci_generator(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# Exemplu de utilizare
# n = int(input("Introdu numărul de termeni: "))
# for numar in fibonacci_generator(n):
#     print(numar)