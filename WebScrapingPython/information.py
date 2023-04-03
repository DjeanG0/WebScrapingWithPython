import requests
from bs4 import BeautifulSoup

url = 'https://www.josecodetech.es'
web = requests.get(url)

soup = BeautifulSoup(web.text, 'lxml')

soup.prettify

cards = soup.find_all('div', attrs={"class": "card"})
cards

list_links = []
for card in cards:
    print ('*'*30)
    print(card)
    print ('*'*30)
    print('\n')
    link = card.find('a')
    print (link.get('href'))    #print attribute href
    list_links.append(link.get('href'))   #join the links to the list
list_links
                    
# Delete dot from links and create url completely
list_urls = []
for link in list_links:
    print(link[1:len(link)])          #Delete dot from links
    link = link[1:len(link)]
    new_url = url + link        #Create url completely         
    print(new_url)
    list_urls.append(new_url)        
list_urls        
   
# Visit all links and get links
title_list = []
youtube_list_links = []                 
for url in list_urls:
    new_web = requests.get(url)
    soup = BeautifulSoup(new_web.text,'lxml')
    cards = soup.find_all('div', attrs={'class': 'card'})
    for card in cards:
        titles = soup.find_all('h3', attrs={'class': 'card-text'})
        #print(titles)
        for title in titles:
            title_list.append(title.text.strip())
            #youtube link
            youtube_links = soup.find_all('figure')
            for link in youtube_links:
                youtube_list_links.append(link.find('iframe').get('src'))
title_list
print('*'*50)
youtube_list_links

#create dictionary with data obtained
data = dict(zip(title_list,youtube_list_links))
data

#data to dataframe
import pandas as pd

print(len(data))
print(type(data))


#Print data in dataframe(table format)
df = pd.DataFrame([[clave, data[clave]] for clave in data.keys()], columns=['Title', 'Link'])
df
df.to_csv('youtubeLinks.csv')  #Save dataFrame in CSV format