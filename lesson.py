from bs4 import BeautifulSoup
import requests

url = 'https://stopgame.ru/'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

#links = soup.find_all('a')
#for link in links:
    #print(link.text)

links = soup.find_all('a')
for link in links:
    print(link.get('href'))

images_tags = soup.find_all('img')
for images_tags in images_tags:
    print(images_tags)

span = soup.find_all('span')
for span in span:
    print(span)

section = soup.find_all('section')
for section in section:
    print(section)

source = soup.find_all('source')
for source in source:
    print(source)