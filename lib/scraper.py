from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)
doc = BeautifulSoup(html.trxt,'html.parser')
 
print(doc.select('.heading-60-black.colour-black mb-20'))

for course in courses:
    print(course.contents[0].strip())


courses = doc.select('.heading-60-black.color-black.mb-20')[0]
name = doc.select('.heading-60-black.color-black.mb-20')[0].name
# => "h2"
doc.select('.heading-60-black.color-black.mb-20')[0].attrs