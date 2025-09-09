'''7. Gestionarea erorilor
Scrie un program care:
•	încearcă să descarce o pagină de la https://httpbin.org/status/404
•	verifică dacă răspunsul are codul de status 200
•	dacă nu, afișează mesajul „Eroare: pagina nu a fost găsită”.'''

import requests

if __name__ == "__main__":
    url = "https://httpbin.org/status/404"
    response = requests.get(url)

    if response.status_code == 200:
        # Dacă răspunsul este OK, poți procesa conținutul aici
        print("Pagina a fost descărcată cu succes.")
        # Poți adăuga cod pentru a procesa răspunsul dacă e nevoie
    else:
        print('Eroare: pagina nu a fost găsită')