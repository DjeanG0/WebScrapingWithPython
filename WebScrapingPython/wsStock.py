import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.expansion.com/mercados/cotizaciones/indices/ibex35_I.IB.html'
r = requests.get(url)
soup= BeautifulSoup(r.content, 'html.parser')
soup

tables = soup.find('table', attrs={'id': 'listado_valores'})
print(tables)

tables = soup.find('table', attrs={'id': 'listado_valores'}).find('tbody')
print(tables)
print('*'*100)

rows = soup.find('table', attrs={'id': 'listado_valores'}).find('tbody').find_all('tr')
print(rows[0])
print('*'*100)

element = rows[0].find_all('td')[0].get_text()    #.text works equally well
print(element)

names = []
for row in rows:
    names.append(row.find_all('td')[0].text)
print(names)
    
value = []
for row in rows:
    value.append(row.find_all('td')[1].text)
print(value)

df = pd.DataFrame({'Names': names, 'Value': value})
df.to_csv('DataFrameExchenge.csv')