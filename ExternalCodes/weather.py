import requests

# api from openweathermap.org
districtName = input("Enter District Name: ")
apikey = '03c0dcc9761cb8f6c56ef511f958d11d'
req = 'https://api.openweathermap.org/data/2.5/weather?q=' + districtName + '&units=metric&appid=' + apikey
response = requests.get(req)
print(response.json())

lat = response.json()['coord']['lat']
print("lat: " + str(lat))
long = response.json()['coord']['lon']
print("long: " + str(long))
weather_main = response.json()['weather'][0]['main']
print("weather main: " + str(weather_main))
weather_description = response.json()['weather'][0]['description']
print("weather description: " + weather_description)
temp = response.json()['main']['temp']
print("temperature:" + str(temp))
temp_feels = response.json()['main']['feels_like']
print("temperature feels like: " + str(temp_feels))
temp_min = response.json()['main']['temp_min']
print("Minimum temperature: " + str(temp_min))
temp_max = response.json()['main']['temp_max']
print("Maximum temperature: " + str(temp_max))
pressure = response.json()['main']['pressure']
print("Pressure: " + str(pressure))
humidity = response.json()['main']['humidity']
print("Humidity:" + str(humidity))
visibility = response.json()['visibility']
print("Visibility: " + str(visibility))
wind_speed = response.json()['wind']['speed']
print("Wind speed: " + str(wind_speed))
wind_deg = response.json()['wind']['deg']
print("Wind deg: " + str(wind_deg))
clouds = response.json()['clouds']['all']
print("Cloud cover: " + str(clouds))

# # api from qoweaer.herokuapp.com
# response = requests.get('https://goweather.herokuapp.com/weather/Dhaka')
# print(response.json())
#
# # api from https://open-meteo.com/en
# # well detailed weather report
# # have to make some extraction from the response
# response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=24.86&longitude=89.33&hourly=temperature_2m')
# print(response.json())
