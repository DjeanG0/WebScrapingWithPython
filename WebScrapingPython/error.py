import requests
from bs4 import BeautifulSoup

url = 'https://www.facebook.com'

try:
    web = requests.get(url)
except Exception as e:
    print('Error accessing facebook{url}')
    
if web.status_code == 200:
    print('Correct response')
else:
    print('Error accessing')    


soup = BeautifulSoup(web.text, 'lxml')

links = soup.find('ul').find_all('a')

if links:
    print('Valid links')
else:
    print('Error on links')