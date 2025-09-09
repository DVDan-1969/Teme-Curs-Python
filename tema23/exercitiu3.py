'''Folosește API-ul gratuit https://wttr.in/?format=j1 pentru a:
•	descărca datele meteo pentru locația implicită
•	afișa temperatura curentă și condițiile de vreme (ex: „Soare”, „Nori”).'''
import requests

if __name__=="__main__":
    url='https://wttr.in/?format=j1'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        data = response.json()
        temperature = data['current_condition'][0]['temp_C']  # Temperatura în grade Celsius
        weather_description = data['current_condition'][0]['weatherDesc'][0]['value']
    print(f"Temperatura curentă: {temperature}°C")
    print(f"Condițiile meteo: {weather_description}")