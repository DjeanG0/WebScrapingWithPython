from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from googletrans import Translator
import requests
from bs4 import BeautifulSoup


# Obtenemos el contenido de la página web
url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
text_to_translate = soup.get_text()

# Creamos una instancia del traductor
translator = Translator(service_urls=['translate.google.com', "https://translate.google.es/",])

# Traducimos el contenido a otro idioma
translated_text = translator.translate(text_to_translate, dest="es").text

# Abrimos una nueva ventana de Chrome
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# Escribimos el texto traducido en la barra de búsqueda de Google
search_box = driver.find_element_by_name("q")
search_box.send_keys(translated_text)
search_box.send_keys(Keys.RETURN)
