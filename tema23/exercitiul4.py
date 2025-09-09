'''4. Descărcarea și salvarea unei imagini
Scrie un program care:
•	descarcă imaginea de la https://httpbin.org/image/png
•	o salvează local sub numele imagine.png.'''

import requests

if __name__ == "__main__":
    url = "https://httpbin.org/image/png"
    response = requests.get(url)

    if response.status_code == 200:
        with open("imagine.png", "wb") as f:
             f.write(response.content)
        print("Imaginea a fost salvată cu succes ca 'imagine.png'.")
    else:
        print(f"Eroare la descărcare: cod status {response.status_code}")
