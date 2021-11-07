import requests

# api from openweathermap.org
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid=03c0dcc9761cb8f6c56ef511f958d11d')
print(response.json())

response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Bogra&appid=03c0dcc9761cb8f6c56ef511f958d11d')
print(response.json())

# api from qoweaer.herokuapp.com
response = requests.get('https://goweather.herokuapp.com/weather/Dhaka')
print(response.json())
response = requests.get('https://goweather.herokuapp.com/weather/Bogura')
print(response.json())


# api from https://open-meteo.com/en
# well detailed weather report
# have to make some extraction from the response
response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=24.86&longitude=89.33&hourly=temperature_2m')
print(response.json())