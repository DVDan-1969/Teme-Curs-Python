'''1.Scrie un program care citeste de la tastatura 2 numere naturale. Daca a > b afiseaza diferenta a - b. Daca a < b afiseaza diferenta b - a.

2.	Intorduceti un numar de 3 cifre de la tastatura. Daca numarul este par afisati suma
dintre numarul introdus si ultima lui cifra. Daca este impar afisati daca este multiplu de 3.

3.	Introduceti de la tastatura un username si o parola. Daca sunt corecte afisati
mesajul ->  {username} s-a logat cu succes si mai departe cereti input-ul user-ului
pentru nume, prenume, e-mail si experienta in IT (ani).
 Daca experienta in IT este mai mica de 1.5 ani, afisati mesajul
-	 {nume} este junior.
 Daca experienta in IT este intre 1.5 si 3 ani, afisati mesajul
-	{nume} este intermediar.
Pentru mai mult de 3 ani experienta afisati mesajul
-	{nume} este senior.
Username-ul si parola sunt corecte daca au valorile hardcoded de mai jos:
user = ‘windows_user’
pass = ‘P@rolla’

4.	Afiseaza care este extensia unui fisier. Numele fisierului se introduce de la tastatura.

5.	Scrie un program care citeste o propozitie de la tastatura. Afiseaza numarul cuvintelor
din acea propozitie

6.	* Fie un semafor programat, pentru pietoni. La inceputul fiecarei ore, timp de 3
minute este verde, dupa care timp de 2 minute este rosu, aceste ferestre de timp de 3,
respectiv 2 minute, continuand pe parcursul intregii ore. Se citeste de la tastatura un
timp t (min). Sa se determine ce culoare are semaforul la timpul t.
ex. t = 14 output: rosu

7.	Afiseaza pe ecran numele  userul-ului din acest string:
command = ‘platform: Solaris; version: 2.5; username: mcristi; all rights reserved to …’

8.	Scrie un program care citeste un mesaj de la tastatura. Daca mesajul este un numar,
ridica-l la puterea a 2-a si afiseaza pe ecran rezultatul. Daca nu este un numar afiseaza
 mesajul pe ecran.

9.	Afiseaza numarul spatiilor dintr-un string. Daca nu exista niciun spatiu scrie
 mesajul “nu exista spatii in string-ul introdus”

10.	Calculeaza suma tuturor cifrelor unui numar introdus de la tastatura. Verifica
daca suma este divizibila cu 8.

11.	Introdu de la tastatura o adresa de e-mail si afiseaza pe ecran domeniul acesteia.
Consideram ca in cadrul adresei de e-mail domeniul se afla dupa caracterul @.
Daca nu are un domeniu, afiseaza un mesaj prin care anunti utilizatorul.

12.	Afiseaza numarul de vocale dintr-o propozitie introdusa de la tastatura.

13.	Afiseaza daca un mesaj de la tastatura poate fi transformat in float. Daca da,
printeaza numarul, altfel afiseaza un mesaj.

14.	Introdu de la tastatura un numar. Daca este mai mare decat 100, aduna cifrele numarului
si afiseaza rezultatul. Daca este mai mic decat 100, inlocuieste numarul cu textul Python
si printeaza-l pe ecran.

15.	Afiseaza True daca o propozitie introdusa de la tastatura incepe cu caracterele ‘Python’.
 Altfel afiseaza False.'''

'''Rezolvare:'''

#5
# x = input('Introduceti propozitia:')
# y = x.split(" ")
# print(y)
# print(len(y))

#6
# t = int(input("Introduceti timpul in minute : "))  # Minutes:0,1,2-verde,Minutes:3,4-rosu
# pozitie_in_ciclu = t % 5
# if pozitie_in_ciclu < 3:
#     print("verde")
# else:
#     print("rosu")

#7
# command = 'platform: Solaris; version: 2.5; username: mcristi; all rights reserved to …'
# a = command.split(";")  # impartim sirul in subsiruri
# b = a[2]
# print(a[2])
# print(b[10:])

#8
# mesaj = input("Introduceti mesajul de la tastatura:")
# try:
#     numar = int(mesaj)  # Încearcă să convertească mesajul într-un număr întreg
#     rezultat = numar ** 2
#     print("Rezultatul (int) ridicat la pătrat este:", rezultat)
# except ValueError:
#     try:
#         numar = float(mesaj)  # Dacă nu e int, încearcă să-l convertească în float
#         rezultat = numar ** 2
#         print("Rezultatul (float) ridicat la pătrat este:", rezultat)
#     except ValueError:
#         print("Mesajul introdus este:", mesaj)  # Dacă nu e număr deloc, afișează mesajul

#9
# sir = input("Introduceti sirul de la tastatura:")
# a = sir.count(" ")
# if a == 0:
#     print("Nu exista spatii in sirul introdus")
# else:
#     print("Numarul de spatii este:", a)

#11
# sir = input("Introduceti de la tastatura adresa de email:")
# a = sir.split("@")
# if len(a[1]) > 1:
#     print("Domeniul este:", a[1])
# else:
#     print("Adresa nu are domeniu")
#12
# propozitie = input("Itroduceti propozitia de la tastatura:")
# vocale = "aeiouAEIOU"  # definim vocalele
# numar_vocale = 0  # initializam un contor
# for caracter in propozitie:  # parcurgem fiecare caracter din propozitie
#     if caracter in vocale:
#         numar_vocale += 1
#         print("Numărul de vocale este:", numar_vocale)
#13
# mesaj = input("Introduceti mesajul de la tastatura:")
# try:
#     numar = float(mesaj)
#     print("Numarul este:", numar)
# except ValueError:
#     print("Mesajul nu poate fi transfotmat in float")
#15
# propozitie = input("Introdu o propozitie: ")
# if propozitie.startswith("Python"):
#     print(True)
# else:
#     print(False)




