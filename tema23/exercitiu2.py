'''2. Trimiterea de parametri prin URL
Scrie un program care:
•	face un GET la https://httpbin.org/get cu parametrii nume=Ion și varsta=25
•	afișează răspunsul în format JSON.'''
import requests

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    parametri = {
        'nume': 'Ion',
        'varsta': '25'
        }
    response = requests.get(url, params=parametri)
    data = response.json()
    print("Cod de status:", response.status_code)
    print("URL complet generat:", data['url'])
    print("Parametrii primiți de server:")
    for cheie, valoare in data['args'].items():
        print(f"  {cheie}: {valoare}")
