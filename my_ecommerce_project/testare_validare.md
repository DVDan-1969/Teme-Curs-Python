TESTARE MANUALA-MY_ECOMMERCE_PROJECT

T1-Login cu date corecte|Utilizator existent|1.Acceseaza/accounts/login/2.Introdu user si parola corecte.3.Apasa login
   Utilizatorul este autentificat redirectionat catre pagina principala admin,numele utilizatorului apare in meniu.
T2-Login cu date incorecte|1.Acceseaza pagina de login.|2.Introdu user si parola gresite.|3.Apasa login.Mesaj de eroare,
   utilizatorul ramane pe aceeasi pagina.
T3-Utilizator autentificat.|1.Apasa Logout.|Sesiunea se inchide,utilizatorul este redirectionat catre login.
T4-Vizualizare lista produse.|Exista cel putin un produs disponibil.|1.Acceseaza /shop/products/|Toate produsele 
   disponibile sunt afisate cu nume,pret si detalii.
T5-Vizualizare detalii produs.|Exista produs.Apasa pe un produs din lista.|Se afiseaza nume,pret,descriere,formular 
   adaugare in cos.
T6-Adaugare produs in cos|Utilizator autentificat,produs existent.|1.Acceseaza pagina produsului.|2.Selecteaza cantitatea
   3.Apasa adauga in cos.Utilizatorul este directionat la shop/cart.Se afiseaza produsele in cos,totalul este calculat
   corect.
T7-Vizualizare cos|Exista produse in cos.|1.Acceseaza shop/cart/|Se afiseaza toate produsele din cos,totalul este 
   afisat corect.
T8-Golire cos.|Exista produse in cos.|1.Acceseaza shop/cart/.|2.Apasa goleste cosul.|Cosul este gol.
T9-Checkout cu produs in cos.|Acceseaza shop/checkout/|Se afiseaza formularul de adresa,totalul comenzii.
T10-Efectuare plata.|1.Acceseaza shop/checkout/|2.Apasa Plateste cu cardul.|3.Utilizatorul este directionat catre pagina 
    Stripe unde utilizatorul introduce datele cardului si face plata.