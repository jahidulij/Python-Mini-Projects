import requests

API_KEY = "54aa6b8a0d2af36470202d45e50634f8"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")
request_url = "{}?appid={}&q={}".format(BASE_URL, API_KEY, city)
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round((data["main"]["temp"] - 273.15), 2)
    print("Weather: " + weather + "\nTemperature: " + str(temperature))
else:
    print("An error occured.")
