import requests
from bs4 import BeautifulSoup

url = 'https://www.josecodetech.es'
web = requests.get(url)

soup = BeautifulSoup(web.text, 'lxml')

soup.prettify

card = soup.find('div', attrs={'class': 'card'})
image = card.find('img').get('src')
image = image[1:len(image)]
image

link_image = url + image
print (link_image)

if len(link_image)==0:
    print('No link found')
else:
    print(link_image)
    
from IPython.display import Image  #to show images

Image(link_image)

#for each image

cards = soup.find_all('div', attrs={"class": 'card'})
#print (cards)
link_images = []
for card in cards:
    image = card.find('img').get('src')
    image = image[1:len(image)]
    link_image = url + image
    link_images.append(link_image)
link_images

Image(link_images[6])
