'''1.	Vehicule
	Creează clasa Vehicle cu atribute: brand, year.
	Creează subclase Car și Bike care adaugă atribute specifice (seats pentru Car si speeds pentru Bike).
	Adaugă metode care afișează informațiile despre fiecare obiect.'''
# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#     def display_info(self):
#         print(f'Brand: {self.brand}')
#         print(f'Year: {self.year}')
#
# class Car(Vehicle):
#     def __init__(self, brand, year,seats):
#         super(). __init__ (brand, year)
#         self.seats = seats
#
#     def display_info(self):
#         super().display_info()
#         print(f'seats: {self.seats}')
#
# class Bike(Vehicle):
#     def __init__(self, brand, year,speeds):
#         super(). __init__ (brand, year)
#         self.speeds = speeds
#
#     def display_info(self):
#         super().display_info()
#         print(f'speeds: {self.speeds}')
#
# if __name__ == '__main__':
#     car1=Car('Hyunday',2005,5)
#     byke1=Bike('Gilmore',2020,8)
#     print('Informatii despre masina:')
#     car1.display_info()
#     print('\nInformatii despre bicicleta:')
#     byke1.display_info()

'''2.	Angajați
	Creează clasa Employee cu atribute: name, salary.
	Creează subclase Developer și Designer care adaugă atribute specifice (ex: limbaj de programare, soft de design).
	Suprascrie metoda __str__() pentru afișare diferită în fiecare subclasă.'''


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def __str__(self):
#         return f"Employee: {self.name}, Salary: {self.salary}"
#
# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, salary)
#         self.programming_language = programming_language
#
#     def __str__(self):
#         return (f"Developer: {self.name}, Salary: {self.salary}, "
#                 f"Programming Language: {self.programming_language}")
#
# class Designer(Employee):
#     def __init__(self, name, salary, design_soft):
#         super().__init__(name, salary)
#         self.design_soft = design_soft
#
#     def __str__(self):
#         return (f"Designer: {self.name}, Salary: {self.salary}, "
#                 f"Design Software: {self.design_soft}")
#
#
# dev = Developer("Ion Popescu", 5000, "Python")
# des = Designer("Maria Ionescu", 4500, "Adobe Photoshop")
#
# print(dev)
# print(des)
'''3.	Animale
	Creează clasa Animal cu metoda make_sound().
	Creează subclase Dog, Cat, Cow, fiecare suprascrie metoda cu sunetul specific.
	Creează o listă de animale și parcurge-o apelând metoda make_sound() pentru fiecare.'''

# class Animal:
#     def make_sound(self):
#         print("Acest animal face un sunet.")

# Subclasa pentru câine
# class Dog(Animal):
#     def make_sound(self):
#         print("Ham Ham!")
#
# # Subclasa pentru pisică
# class Cat(Animal):
#     def make_sound(self):
#         print("Miau Miau!")
#
# # Subclasa pentru vacă
# class Cow(Animal):
#     def make_sound(self):
#         print("Muuu Muuu!")
#
# # Crearea unei liste de animale
# animals = [Dog(), Cat(), Cow()]

# Parcurgerea listei și apelarea metodei make_sound()
# for animal in animals:
#     animal.make_sound()
'''4.	Forme geometrice
	Creează clasa Shape cu metoda area() (fără implementare, doar ridică NotImplementedError).
	Creează subclase Rectangle, Circle, Triangle care implementează area().
	Creează o listă de forme și calculează aria totală.'''
# from math import pi
#
# class Shape:
#     def area(self):
#         raise NotImplementedError("Metoda 'area' trebuie să fie implementată de subclasă")
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
# shapes = [
#     Rectangle(5, 10),
#     Circle(7),
#     Triangle(6, 8)
# ]
# total_area = sum(shape.area() for shape in shapes)
#
# print(f"Aria totală a formelor este: {total_area}")
'''6.	Bibliotecă și cărți digitale
Creează clasa Book cu atribute title, author.
Creează subclasa EBook care adaugă file_size și format.
Creează clasa Library care poate stoca atât cărți normale, cât și ebooks.
Adaugă metode pentru a lista cărțile și a calcula spațiul total ocupat de ebooks.'''

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return f'"{self.title}" de {self.author}'
#
# class EBook(Book):
#     def __init__(self, title, author, file_size, file_format):
#         super().__init__(title, author)
#         self.file_size = file_size  # în MB
#         self.file_format = file_format
#
#     def __str__(self):
#         return f'"{self.title}" de {self.author} [{self.file_format}, {self.file_size}MB]'

# Clasa Library care stochează atât Book cât și EBook
# class Library:
#     def __init__(self):
#         self.books = []  # listă cu obiecte Book și EBook
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def list_books(self):
#         if not self.books:
#             print("Biblioteca este goală.")
#         else:
#             print("Cărți în bibliotecă:")
#             for id, book in enumerate(self.books, 1):
#                 print(f"{id}. {book}")
#
#
#     def total_ebook_size(self):
#             total_size = sum(book.file_size for book in self.books if isinstance(book, EBook))
#             return total_size
#adună toate valorile generate de expresia generatorului din interior.
#fiecare book, verifică dacă este o instanță a clasei EBook folosind isinstance(book, EBook).

# if __name__ == "__main__":
#     library = Library()
#
#     book1 = Book("Enigma Otiliei", "George Călinescu")
#     ebook1 = EBook("Python Programming", "John Zelle", 5.6, "PDF")
#     ebook2 = EBook("Clean Code", "Robert C. Martin", 3.2, "EPUB")
#
#     library.add_book(book1)
#     library.add_book(ebook1)
#     library.add_book(ebook2)
#
#     library.list_books()
#
#     print(f"\nSpațiu total ocupat de ebooks: {library.total_ebook_size()} MB")

'''Folosim functia enumerate pentru a parcurge lista self.books.Functia returnează o pereche formată din index 
și element pentru fiecare element din listă.Numerotarea incepe de la 1.Fiecare element din self.books, idx va 
avea valoarea poziției în listă,'''

'''7.	Vehicule electrice
	Clasa de bază Vehicle (atribute: brand, year).
	Subclasă Car (atribute: seats).
	Subclasă ElectricCar (atribute: battery_capacity).
	Adaugă metode pentru a calcula autonomia (ex: range = battery_capacity * 5 km).'''

# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
# class Car(Vehicle):
#     def __init__(self, brand, year, seats):
#         super().__init__(brand, year)
#         self.seats = seats
#
# class ElectricCar(Car):
#     def __init__(self, brand, year, seats, battery_capacity):
#         super().__init__(brand, year, seats)
#         self.battery_capacity = battery_capacity  # în kWh
#
#     def calculate_range(self):
#         # Calculul autonomiei în km
#         return self.battery_capacity * 5
#
# if __name__ == "__main__":
#     electric_car = ElectricCar("Tesla", 2022, 5, 75)
#     print(f"Marca: {electric_car.brand}")
#     print(f"An: {electric_car.year}")
#     print(f"Număr de locuri: {electric_car.seats}")
#     print(f"Capacitate baterie: {electric_car.battery_capacity} kWh")
#     print(f"Autonomie estimată: {electric_car.calculate_range()} km")

