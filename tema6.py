'''Se definesc listele de mai jos:
       lst_1 = [1, 2, 3, 4]
        lst_2 = [1, 2, 3, 4]
        print(lst_1 == lst_2, lst_1 is lst_2)
Ce este afisat?
a.	True True
b.	True False
c.	False True
d.	False False

De ce ai facut aceasta alegere?

      2. Afisati cel mai mare numar dintr-o lista. Lista poate sa contina orice tip de date.

      3. Eliminati dintr-o propozitie data ca input, toate cuvintele care incep cu litera A (a).
      Afisati propozitia rezultata fara acele cuvinte.

      4. Afisasti suma celor mai mici doua numere pozitive dintr-o lista.
Varianta 1: Lista contine doar intregi pozitivi -> numbers = [5, 3, 100, 1, 435, 1000]
Varianta 2: Lista contine numere intregi pozitive si negative -> numbers = [1, -4, 10, 18, -53, -33]


      5*. Se citeste un numar intreg, de 4 cifre, de la tastatura. Afisati care este urmatorul numar de 4 cifre, cu toate cifrele distincte
Ex: 1003 -> 1023

      6.* Afla care este cel mai mare prefix comun al cuvintelor date intr-o lista:
Ex: input: words = ['frig','frumos','frate']
output: fr

input: words = ['Python' , 'Pasare', 'Politie']
output: P

input: words = ['curajos', 'curat', 'custodie']
output: cu

      7. Se da o lista cu elementele stringuri. Afiseaza o lista in care cuvintele din lista data ca input sunt scrise invers (de la dreapta la stanga)
words = [‘python’, ‘ruby’, ‘javascript’]
Output: new_words = [‘nohtyp’, ‘ybur’, ‘tpircsavaj’]

      8. Se da o lista de cuvinte. Afisati cuvintele care au un numar de caractere mai mare decat valoare medie a caracterelor din lista.


     9. Sa da urmatorul string:
name = 'first-name'
Convertiti acest string intr-unul snake_case'''
#2
# lista =[1,2,3,"a","b",5,8,"d"]
# numere=[]
#     # Filtrăm doar numerele (int sau float) folosind type()
# for element in lista:
#     if type(element) == int or type(element) == float:
#             numere.append(element)
#     # Dacă există numere, afișăm cel mai mare dintre ele
#     if numere:
#         print("Cel mai mare numar este:", max(numere))
#     else:
#         print("Nu există numere în listă.")
#3
# txt=input("Introduceti propozitia de la tastatura:")
# cuvinte=[]
# x=txt.casefold()
# y=x.split(" ")
# print(y)
# for element in y:
#     if element[0]!='a':
#         cuvinte.append(element)
#     print(cuvinte)
#4
# list1=[5, 3, 100, 1, 435, 1000]
# list2=[1, -4, 10, 18, -53, -33]
# pozitivi = [num for num in list1 if num > 0]
# pozitivi.sort()
# rezultat=pozitivi[0]+pozitivi[1]
# print(rezultat)

#6
# words1 = ['frig','frumos','frate']
# output1=[]
# for element in words1:
#     if len(element) > 0 and element[0] == 'f':
#         output1.append(element[0])
#     print(output1)
#     if len(element) > 1 and element[1] == 'r':
#         output1.append(element[1])
#     print(output1)
#     if len(element) > 2 and element[2] == 'i':
#         output1.append(element[2])
#     print(output1)
#     if len(element) > 3 and element[3] == 'g':
#         output1.append(element[3])
#     print(output1)

#7
# words = ['python', 'ruby', 'javascript']
# new_words = []
# for element in words:#parcurgem lista words
#     reversed_word = ''#la fiecare iteratie se creaza un string gol pt. cuvantul inversat
#     for char in element:#se parcurge fiecare caracter
#         reversed_word = char + reversed_word  #caracterul se adauga in fata stringului
#     new_words.append(reversed_word)#cuvantul inversat se adauga la lista
# print(new_words)
#9
# a='first-name'
# b=a.replace('-','_')
# print(b)


