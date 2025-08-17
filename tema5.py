'''1 Afisati toate numerele pare intre 0 si 3000.

2.* Afisati toate numerele prime intre 0 si 1000.

3.Definiti in program (hardcoded) un numar.
Introduceti de la tastatura numere pana cand l-ati ghicit pe cel hardcoded.
Puteti sa afisati indicii (mai mult, mai putin, ai castigat).

4.Creati meniul unei aplicatii. Meniul trebuie sa accepte introducerea unei
taste de la tastatura pentru a continua cu executia acelei functionalitati.
Ex.
Press 1 to enter the user name
Press 2 to enter the  password
Press 3 to enter the  e-mail
Press 4 to show the details (user, password, e-mail)
Press E/e to exit the program
5.Afisati cate vocale contine un text pe care il introduceti de la tastatura.
   	Afisati si numarul consoanelor.

6.Se introduc de la tastatura 2 string-uri. Cate caractere comune au cele 2 string-uri si care sunt acestea?

7.Introduceti de la tastatura un numar natural n. Calculat n!, afisand rezultatatul.
Ex. 4! = 1 * 2 * 3 * 4
9! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9

8.	Se introduce de la tastatura o propozitie. Afisati pe ecran string-ul format din caractere distincte (se elimina duplicatele)
9.	 Se da un string s. Sa se printeze numarul total de litere, numarul digitilor, numarul simbolurilor si numarul spatiilor din cadrul stringului.
 Ex. input s = 'Abgks562als9!!@(js'
 output: char: 10 digits: 4 simbols: 4 spaces: 0'''
#1
# x=range(0,3001,2)
# for a in x:
#     print(a)

#3
# numar =25
# while True:
#     numar2=int(input("Introduceti un numar de la tastatura:"))
#     if numar2<numar:
#         print("Numarul2 este mai mic decat numar")
#     elif numar2>numar:
#         print("Numaru2 este mai mare decat numar")
#     else:
#         print("Numar2 este egal cu numar")
#         break
#5
# propozitie=input("Itroduceti propozitia de la tastatura:")
# vocale = "aeiouAEIOU"#definim vocalele
# numar_vocale = 0#initializam un contor
# for caracter in propozitie:#parcurgem fiecare caracter din propozitie
#     if caracter in vocale:
#         numar_vocale += 1
#         print("Numărul de vocale este:", numar_vocale)
# consoane ="bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ"
# numar_consoane=0#initializare contor
# for caracter in propozitie:
#     if caracter in consoane:
#         numar_consoane+=1
#         print("Numarul de  consoane este:",numar_consoane)

#6
# string1 = input("Introdu primul string: ")
# string2 = input("Introdu al doilea string: ")
# set1 = set(string1)# convertim stringurile in set-uri,eliminam duplicatele
# set2 = set(string2)
# caractere_comune = set1.intersection(set2)#gasim caracterele comune
# print(f"Caracterele comune sunt: {caractere_comune}")
# print(f"Numarul de caractere comune este: {len(caractere_comune)}")

#7
# n=int(input("Introduceti numarul de la tastatura:"))
# result=1
# for i in range (1,n+1):
#     result*=i
# print("Factorialul lui n este:",result)
#8
# sir=input("Introduceti propozitia de la tastatura:")
# sir_fara_duplicate=[]
# for char in sir:
#     if char not in sir_fara_duplicate:
#         sir_fara_duplicate.append(char)
# print(sir_fara_duplicate)


#9
# string=input("Introduceti sirul de la tastatura:")
# litere = 0
# cifre = 0
# simboluri = 0
# spatii = 0
# for caracter in string:
#     if caracter.isalpha():
#         litere += 1
#     elif caracter.isdigit():
#         cifre += 1
#     elif caracter.isspace():
#         spatii += 1
#     else:
#         simboluri += 1
# print("Numărul de litere:", litere)
# print("Numărul de cifre:", cifre)
# print("Numărul de simboluri:", simboluri)
# print("Numărul de spații:", spatii)



