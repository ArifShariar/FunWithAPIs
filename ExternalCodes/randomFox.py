import re
import urllib
import requests
from bs4 import BeautifulSoup
import cv2
response = requests.get('https://randomfox.ca/floof/')
fox_images = response.json()
print(fox_images)
print(fox_images['image'])
print(fox_images['link'])


# download images from url
# and open it using opencv
numbers = re.findall('[0-9]+', fox_images['link'])
res = requests.get(fox_images['image'])
file_name = 'fox' + numbers[0] + '.jpg'
with open(file_name, 'wb') as f:
    f.write(res.content)
    f.close()
    print("download complete")
    img = cv2.imread(file_name)
    cv2.imshow('image', img)
    cv2.waitKey(0)

