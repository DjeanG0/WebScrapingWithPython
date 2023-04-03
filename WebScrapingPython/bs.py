import requests
from bs4 import BeautifulSoup

url = 'https://www.facebook.com'
web = requests.get(url)

web.status_code     #obtain the status code

print(web.text)

soup = BeautifulSoup(web.text, 'lxml')
soup

soup.find('ul') #obtain the first element of ul

links = soup.find('ul').find_all('a') #get links of the above elements
link = links[0]   #get the first link
link.get('href') #get link
link.get_text()
links = [link.get('href') for link in links]   #get all links
links

#to obtain files from main url, with loops can go deeper
newUrl = links[0]
newWeb = requests.get(newUrl)
newWeb.status_code
newSoup = BeautifulSoup(newWeb.text, 'lxml')
print(newSoup)

soup.find('div', attrs={'class':'card'})   #search class for attribute and value

