'''1.	Dureaza mai mult sa adaugi elemente cu append intr-o lista sau sa folosesti list comprehension?
Creeaza 2 functii care returneaza timpul necesar celor 2 operatiuni.
Poti folosi time.time() pentru a obtine timpul curent.

2.	Se da un string s. Scrie o functie care returneaza suma caracterelor de tip cifra din s.
Modifica functia astfel incat sa returneze suma numerelor din s. Un numar este reprezentat de caractere numerice alaturate. 
ex:
s = 'eu am 33 de ani. in 2 luni va fi ziua mea de nume'
result: 35

3.	Scrieti o functie care primeste un numar variabil de argumente de tip lista si returneaza o lista cu toate elementele argumentelor.

4.	 Scrieti o functie care primeste numele unui fisier ca parametreu si returneaza tipul acelui fisier.
ex:
def file_type(file_name):
	pass

file_type(‘20221107.jpeg’) -> imagine
file_type(‘test.txt’’) -> text
file_type(‘music_20221107.mp3’) -> muzica

5.	Scrieti o functie care determina daca un cuvant contine litere care nu se repeta (este format din caractere unice)
Functia poate returna True sau False

6.	* Se da un numar. Scrie o functie care returneaza numarul ca un string in urmatorul format:
Input: 37 → output: ‘30 + 7’
Input: 114 → output: ‘100 + 10 + 4’
Input: 30165 → output: ‘30000 + 100 + 60 + 5’

7.	Scrie o functie care returneaza cuvantul cu scorul cel mai mare.
Scorul unui cuvant este dat de suma pozitiilor literelor cuvantului, din alfabet.
Functia primeste ca argument o lista de cuvinte.
ex: 
a = 1, b = 2, c = 3, d = 4, etc
Word: mama, scor: 13 + 1 + 13 + 1 = 30


8.	Se dau 3 tupluri ca input. Fiecare dintre aceste tupluri contine urmatoarele informatii (nume, varsta, inaltime) Afiseaza cele 3 tupluri, dupa sortarea (a-z) si in ordine crescatoare, tinand cont, pe rand, de nume, varsta si inaltime. 
Ex. 
input: (Dan, 33, 170), (Mihai, 20, 180), (Daniel, 40, 173) 
dupa nume: (Dan, 33, 170), (Daniel, 40, 173), (Mihai, 20, 180) 
dupa varsta: (Mihai, 20, 180), (Dan, 33, 170), (Daniel, 40, 173) 
dupa inaltime: (Dan, 33, 170), (Daniel, 40, 173), (Mihai, 20, 180)

9.	Se da o lista de intregi. Pentru fiecare element din lista sa se determine cate numere din cadrul acelei liste sunt mai mici decat acel element. Rezultatul se returneaza tot intr-o lista 
Ex. nbs = [3, 7, 8, 5] 
output: [0, 2, 3, 1] 
pentru nbs[0] = 3 nu exista niciun numar mai mic in nbs pentru nbs[1] = 7 exista 2 numere mai mici,  etc.

10.	* Fie un intreg pozitiv n, dat ca input. Scrie o aplicatie care sa printeze o forma triunghiulara realizata din caracterul '*'.
n reprezinta numarul de randuri ale acestui pattern. Numarul de pe fiecare rand va creste cu 2.

Ex. input n = 3
output: 
*
***
*****

input: n = 5
output: 
*
***
*****
*******
*********

11.	Fie un string s care contine cuvinte separate de unul sau mai multe spatii. Sa se returneaza un string cu toate cuvintele inversate si separate de un singur spatiu.

Ex. input s = 'python java        javascript'
output: 'javascript java python'''''
#1
# import time
# def timpul_append(n):
#     lista = []
#     start_time = time.time()
#     for i in range(n):
#         lista.append(i)
#     end_time = time.time()
#     return end_time - start_time
#
# def timpul_list_comprehension(n):
#     start_time = time.time()
#     lista = [i for i in range(n)]
#     end_time = time.time()
#     return end_time - start_time
# n = 10**6  # numărul de elemente
# print(f"Timp pentru append(): {timpul_append(n)} secunde")
# print(f"Timp pentru list comprehension: {timpul_list_comprehension(n)} secunde")

#2
# s = input("Introduceti sirul de la tastatura: ")
#
# def suma_caractere_cifra():
#     total = 0
#     for char in s:  # parcurgem fiecare caracter
#         if char.isdigit():  # dacă caracterul este o cifră
#             total += int(char)
#     return total  # returnăm totalul după ce am terminat bucla
# suma = suma_caractere_cifra()
# print("Suma caracterelor de tip cifra este:", suma)
#
# def suma_numerelor():
#     total = 0
#     fragmente = s.split()
#     for frag in fragmente:
#         try:
#             numar = int(frag) # Încearcă să convertești fragmentul într-un număr
#             total += numar
#         except ValueError:
#               continue # Dacă nu se poate converti, ignorăm
#     return total
# print(suma_numerelor())


#3
# input_string = input("Introdu o listă de numere, separate prin virgulă: ")
# lista1 = [int(x) for x in input_string.split(',')]
# print(lista1)
# input_string = input("Introdu o listă de cuvinte, separate prin spațiu: ")
# lista2 = input_string.split()
# print(lista2)
# def combina_liste(*args):
#     rezultat = []
#     for lista in args:
#         rezultat.extend(lista)
#     return rezultat
# lista_combinata = combina_liste(lista1, lista2)
# print("Lista combinată:", lista_combinata)

#4
# input_string=input("Introduceti fisierul de la tastatura:")
# def file_type(file_name):
#     dot_position = file_name.find('.')
#     if dot_position == -1:
#         return "Fisierul nu are extensie"
#     else:
#          return file_name[dot_position + 1:]
# tip_fisier = file_type(input_string)
# print("Tipul fișierului este:", tip_fisier)

#5
# cuvant=input("Introduceti sirul de la tastatura:")
# def are_caractere_unice(cuvant):
#     caractere_unice = set(cuvant) # Convertim cuvântul în set pentru a elimina duplicatele
#     return len(cuvant) == len(caractere_unice)# Comparam lungimea setului cu lungimea cuvântului
# print(are_caractere_unice(cuvant))

#6
# str_input=input("Introduceti numarul de la tastatura:")
# def descompunere_numar():
#     cifre = list(str_input)
#     lungime = len(cifre)
#     termeni = []
#
#     for i, cifra in enumerate(cifre):
#         if cifra != '0':
#             valoare = int(cifra) * (10 ** (lungime - i - 1))
#             termeni.append(str(valoare))
#             print(termeni)
#     return" + ".join(termeni)# trimite stringul rezultat înapoi
# print(descompunere_numar())

#8
# tuple1=("Dan", 33, 170)
# tuple2=("Mihai", 20, 180)
# tuple3=("Daniel", 40, 173)
# lista_tupluri = [tuple1, tuple2, tuple3]#facem o variabila care contine tupluri
# def sorteaza_dupa(criteriu):
#     return sorted(lista_tupluri, key=criteriu)
#
# tupluri_dupa_nume = sorteaza_dupa(lambda x: x[0])#x[0] este nume
# print("Sortate după nume:", tupluri_dupa_nume)
#
# tupluri_dupa_varsta = sorteaza_dupa(lambda x: x[1])#x[1] este varsta
# print("Sortate după vârstă:", tupluri_dupa_varsta)
#
# tupluri_dupa_inaltime = sorteaza_dupa(lambda x: x[2])#x[2] este inaltimea
# print("Sortate după înălțime:", tupluri_dupa_inaltime)

#9
# input_string = input("Introdu o listă de numere, separate prin virgulă: ")
# lista1 = [int(x) for x in input_string.split(',')]
# print(lista1)
# def count_smaller_elements():
#     result = []
#     for num in lista1:
#         count = sum(1 for x in lista1 if x < num)
#         result.append(count)
#     return result
# print(count_smaller_elements())

#11
# s=input("Introduceti sirul de la tastatura:")
# def inverseaza_cuvinte(s):
#     cuvinte = s.split()
#     cuvinte_inversate = [cuvant[::-1] for cuvant in cuvinte]# Inversează fiecare cuvânt
#     rezultat = ' '.join(cuvinte_inversate) # Reunește cuvintele inversate într-un singur string, separate prin spațiu
#     return rezultat
# print(inverseaza_cuvinte(s))

