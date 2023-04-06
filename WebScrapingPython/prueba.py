import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Obtiene el contenido HTML de una página web
def get_html(url):
    response = requests.get(url)
    return response.text

# Traduce el contenido de un texto a otro idioma
def translate_text(text, dest='en'):
    translator = Translator()
    return translator.translate(text, dest=dest).text

# Traduce el contenido HTML de una página web a otro idioma
def translate_html(html, dest='en'):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all(True):
        if tag.string:
            tag.string.replace_with(translate_text(tag.string, dest=dest))
    return str(soup)

# Ejemplo de uso
url = 'https://es.wikipedia.org/wiki/Python'
html = get_html(url)
translated_html = translate_html(html, dest='es')
print(translated_html)