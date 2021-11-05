# read an html file and extract all the images
import re
import requests
from bs4 import BeautifulSoup

response = requests.get('https://randomfox.ca/floof/')
fox_images = response.json()
print(fox_images)
print(fox_images['image'])
print(fox_images['link'])

numbers = re.findall('[0-9]+', fox_images['link'])
print(int(numbers[0]))
