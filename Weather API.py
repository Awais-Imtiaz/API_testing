import requests

API_KEY = "API_KEY"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"The temperature of {city} is : " , end = "")
    print(data['main']['temp'])
else:
    print("Error:", response.status_code)
