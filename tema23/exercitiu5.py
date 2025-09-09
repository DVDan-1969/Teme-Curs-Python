'''6. Trimiterea unui request POST cu date
Scrie un program care:
•	trimite un POST la https://httpbin.org/post cu un payload JSON: {"utilizator": "admin", "parola": "1234"}
•	afișează răspunsul în format JSON.'''
import requests

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {'utilizator': 'admin', 'parola': '1234'}
    response = requests.post(url, json=payload)
    data = response.json()
    print("Cod de status:", response.status_code)
    print("URL-ul cererii:", data['url'])
    print("Datele trimise în corpul cererii:")
    for cheie, valoare in data['json'].items():
        print(f"  {cheie}: {valoare}")

