'''1. Scrie un program care citește un fișier input.txt și afișează numărul total de linii.
2. Citește un fișier și numără câte cuvinte conține în total.
3. Primește un șir de la utilizator și scrie-l într-un fișier output.txt.
4. Citește conținutul din source.txt și scrie-l identic în destination.txt.
5. Cere utilizatorului un cuvânt și afișează doar liniile din fișierul text.txt care îl conțin.
6. Citește un fișier input.txt și scrie în output.txt liniile în ordine inversă.
7. * Fișierul numbers.txt conține câte un număr pe fiecare linie. Scrie într-un alt fișier
 doar numerele pare. Programul trebuie sa functioneze inclusiv daca pe o linie se afla un
 non-numar.
8. Scrie un program care citește un fișier și creează un nou fișier în care tot textul este
transformat în litere mari.

Incercati sa faceti rezolvarile in cadrul unor functii, unde e cazul, si organizati rularea
codului in acel ‘ if __name__ == “__main__”: ‘. Obisnuiti-va sa va pastrati munca organizata
in acest format.'''
#1
# numar_linii=0
# with open("input.txt","rt") as fisier:
#     for linie in fisier:
#         numar_linii+=1
# print("Numarul total de linii este:",numar_linii)
#2
# numar_cuvinte=0
# with open("input.txt","r") as fisier:
#     for linie in fisier:
#         cuvinte=linie.split(" ")
#         numar_cuvinte+=len(cuvinte)
# print("Numarul total de cuvinte:",numar_cuvinte)
#3
# str_input = input("Introduceți sirul: ")
# with open("output.txt", "w") as fisier:# Deschide fișierul pentru scriere (crează sau suprascrie)
#     fisier.write(str_input)#
# with open("output.txt") as fisier:
#     print(fisier.read())# Afișează conținutul fișierului
#4
# def copiaza_fisier(source_file,destination_file):
#     with open("source.txt", "rt") as fisier:
#         continut = fisier.read()
#         print(continut)
#     with open("destination.txt", "w") as fisier:
#         fisier.write(continut)
#     with open("destination.txt", "rt") as fisier:
#         print(fisier.read())
# if __name__ == "__main__":
#              copiaza_fisier("source.txt","destination.txt")
#5
# cuvant=input("Introduceti cuvantul:")
# with open ("text.txt","rt") as fisier:
#     for linie in fisier:
#         if cuvant in linie:
#             print(linie.strip())
#6
# def linii_in_ordine_inversa(input_file,output_file):
#     with open(input_file, 'r') as fisier:
#         lines = fisier.readlines()
#     lines_inversate = lines[::-1]
#     with open(output_file, 'w') as fisier:
#         fisier.writelines(lines_inversate)
#     with open(output_file, "r") as fisier:
#         print(fisier.read())
# if __name__ == "__main__":
#             linii_in_ordine_inversa("input.txt","output.txt")
#8
# def transforma_in_litere_mari(input_file, output_file):
#     with open(input_file, 'r') as fisier:
#         continut = fisier.read()
#         continut_mare = continut.upper()
#     with open(output_file, 'w') as fisier:
#         fisier.write(continut_mare)
#     with open(output_file, "rt") as fisier:
#         print(fisier.read())
# if __name__ == "__main__":
#             transforma_in_litere_mari('input.txt', 'output.txt')

