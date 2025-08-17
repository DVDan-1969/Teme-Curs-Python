'''1.	Scrie un program care cere două numere de la utilizator și încearcă să le împartă. Prinde orice excepție care ar putea apărea (ex: împărțire la zero sau introducere nevalidă).
2.	Definește o listă de 5 elemente și cere un index de la utilizator. Încearcă să
afișezi elementul de la acel index, dar tratează excepția dacă indexul este în afara listei.
3.	* Cere două numere și o operație (+, -, *, /). Încearcă să efectuezi calculul și
să tratezi erorile: împărțire la 0, operare invalidă, date nevalide.
4.	Scrie o funcție safe_divide(a, b) care returnează rezultatul împărțirii, dar:
•	dacă b == 0, returnează "Impartire la zero interzisa!"
•	dacă a sau b nu sunt numere, returnează "Valori invalide"
Folosește try, except, else.
5.	Cere în mod repetat numere de la utilizator și adună-le până când se introduce „stop”.
Folosește try-except pentru a prinde dacă nu se introduce un număr valid.

Incercati sa faceti rezolvarile in cadrul unor functii, unde e cazul, si organizati
 rularea codului in acel ‘ if __name__ == “__main__”: ‘. Obisnuiti-va sa va pastrati
 munca organizata in acest format.'''
#1
# try:
#     n1=int(input("n1="))
#     n2=int(input("n2="))
#     rezultat=n1/n2
# except ZeroDivisionError:
#     print("Eroare:Nu poti imparti cu zero")
# except ValueError:
#     print("Error:Introduceti numere valide")
# except Exception as e:
#     print(f"A aparut o eroare:{e}")
#2
# try:
#     n=int(input("Introduceti un numar dela 0 la 4:"))
#     list = ["mere", "banane", "cirese", "portocale", "caise"]
#     print(list[n])
# except ValueError:
#     print("Indexul este in afara listei")
# except Exception as e:
#     print(f"A aparut eroarea:{e}")
#3
# try:
#     numar1 = int(input("Introduceti primul număr: "))
#     numar2 = int(input("Introduceti  al doilea număr: "))
#     operatie = input("Introdu operația (+, -, *, /): ")
#     if operatie == "+":
#         rezultat = numar1 + numar2
#         print(rezultat)
#     elif operatie == "-":
#         rezultat = numar1 - numar2
#         print(rezultat)
#     elif operatie == "*":
#         rezultat = numar1 * numar2
#         print(rezultat)
#     elif operatie == "/":
#          rezultat = numar1 / numar2
#          print(rezultat)
# except ZeroDivisionError:
#      print("Eroare:Nu poti imparti cu zero")
# except ValueError:
#      print("Error:Introduceti numere valide")
# except TypeError:
#      print("Introduceti acelasi tip de date")
# except Exception as e:
#     print(f"A aparut eroarea:{e}")
#4
# def safe_divide():
#     try:
#         a = float(input("Introduceti primul numar:"))
#         b = float(input("Introduceti al doilea numar:"))
#         rezultat = a/b
#     except ZeroDivisionError:
#         print("Eroare: Împărțirea la zero nu este permisă.")
#     except ValueError:
#         print("Error:Introduceti numere valide")
#     else:
#         print(f"Rezultatul împărțirii este: {rezultat}")
# safe_divide()
#5
# total = 0
# while True:
#     input_str = input("Introduceți un număr sau 'stop' pentru a termina: ")
#     if input_str.lower() == "stop":
#         break
#     try:
#         num = float(input_str)
#         total += num
#     except ValueError:
#         print("Vă rugăm să introduceți un număr valid sau 'stop' pentru a termina.")
# print(f"Suma totală este: {total}")
