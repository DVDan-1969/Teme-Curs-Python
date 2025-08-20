
# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=[]
#
#     def add_grade(self, grade):
#         self.grade.append(grade)
#
#     def calculate_average(self):
#         if not self.grade:#verificăm dacă lista grades este goală,Dacă nu există note, returnăm 0 pentru
#             # a evita împărțirea la zero.
#             return 0
#         return sum(self.grade) / len(self.grade)
#
# if __name__ == '__main__':
#
#     student1 = Student("Ion Popescu", 20, grade=None)
#     student1.add_grade(8)
#     student1.add_grade(9)
#     print(f"Media lui {student1.name} este: {student1.calculate_average():.2f}")

'''6.Clasa „Employee” + Manager
    Creează o clasă Employee cu nume și salariu.
	Creează o subclasă Manager care are și o listă de angajați în subordine.
	Adaugă o metodă care afișează numele tuturor angajaților coordonați de manager.
	Suprascrie __str__() pentru afișare frumoasă.'''
# class Employee:
#     def __init__(self, nume, salariu):
#         self.nume = nume
#         self.salariu = salariu
#
#     def __str__(self):
#         return f"{self.nume} (Salariu: {self.salariu} RON)"
#
#
# class Manager(Employee):
#     def __init__(self, nume, salariu, angajati=None):
#         super().__init__(nume, salariu)
#         self.angajati = angajati if angajati is not None else []
# #setează lista de angajați la valoarea dată dacă există, sau o listă goală dacă nu a fost furnizat nimic
#     def adauga_angajat(self, angajat):
#         self.angajati.append(angajat)
#
#     def afiseaza_angajati(self):
#         print(f"Angajații coordonați de {self.nume}:")
#         for angajat in self.angajati:
#             print(f"- {angajat.nume}")
#
#     def __str__(self):
#         return f"Manager: {self.nume}, Salariu: {self.salariu} RON, Angajați: {[a.nume for a in self.angajati]}"
#
#
# if __name__ == "__main__":
#     # Creăm angajați
#     angajat1 = Employee('Ion', 3000)
#     angajat2 = Employee('Maria', 3500)
#     angajat3 = Employee('Andrei', 3200)
#
#     # Creăm manager și adăugăm angajați
#     manager1 = Manager('Popescu', 8000)
#     manager1.adauga_angajat(angajat1)
#     manager1.adauga_angajat(angajat2)
#     manager1.adauga_angajat(angajat3)
#
#     print(manager1)
#     manager1.afiseaza_angajati()

'''7	Creează o clasă Library care conține o listă de obiecte Book.
	Metode:
	add_book(book)
	find_by_author(author)
    list_books()'''
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return f'"{self.title}" de {self.author}'
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def find_by_author(self, author):
#         return [book for book in self.books if book.author == author]
#
#     def list_books(self):
#         for book in self.books:
#             print(book)
#
#
# if __name__ == "__main__":
#     library = Library()
#
#     # Adaugă câteva cărți
#     library.add_book(Book("Don Quijote", "Miguel de Cervantes"))
#     library.add_book(Book("Prințesa de cleștar", "Vladimir Nabokov"))
#     library.add_book(Book("Marele Gatsby", "F. Scott Fitzgerald"))
#
#     # Afișează toate cărțile
#     library.list_books()
#
#     # Caută cărțile de un anumit autor
#     for book in library.find_by_author("Vladimir Nabokov"):
#         print(book)
