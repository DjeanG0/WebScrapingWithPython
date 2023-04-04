import requests
from bs4 import BeautifulSoup

url = 'https://www.eltiempo.es/duitama.html'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'lxml')
print(web.status_code)

temperature = soup.find('span', attrs={'class': 'c-tib-text'}).get_text()
print(temperature)

section_state = soup.find('div', attrs={'class': 'c-pois-text'})
state = section_state.find('span').get_text()
print(state)

maximum = soup.find('span', attrs={'class': 'm_table_weather_day_max_temp'})
max_temp = maximum.find('span').get_text()
minimum = soup.find('span', attrs={'class': 'm_table_weather_day_min_temp'})
min_temp = minimum.find('span').get_text()


city = soup.find('span', attrs={'class': '-itl'}).get_text().strip()
city

print (f'the temperature now is {temperature} in {city} \nStatus: {state}')
print (f'the maximum temperature is {max_temp}')
print (f'the minimum temperature is {min_temp}')