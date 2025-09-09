'''1. Obținerea conținutului unei pagini web
Scrie un program care:
•	folosește requests.get() pentru a descărca conținutul paginii https://httpbin.org/get
•	afișează codul de status și primele 200 de caractere din textul răspunsului.'''

import requests

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    response = requests.get(url)
    print(response.status_code)
    print("Primele 200 de caractere din răspuns:")
    print(response.text[:200])
