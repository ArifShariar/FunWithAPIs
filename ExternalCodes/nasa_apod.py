import requests

req = requests.get('https://api.nasa.gov/planetary/apod?api_key=JbPh57ub5qcB6frjO0UHzsSxiySqwyiZe7b3WpZe')
print(req.status_code)
print("copyright: " + req.json()['copyright'])
print("date: " + req.json()['date'])
print("explanation: " + req.json()['explanation'])
print("hdurl: " + req.json()['hdurl'])
print("media_type: " + req.json()['media_type'])
print("service_version: " + req.json()['service_version'])
print("title: " + req.json()['title'])
print("url: " + req.json()['url'])


