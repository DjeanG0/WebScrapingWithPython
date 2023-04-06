from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def translate_web_page(file_path, dest_language, output_file_path):
    translator = Translator()
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Leer el contenido del archivo HTML
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    driver.get("data:text/html;charset=utf-8," + content)

    # Esperar a que la página se cargue
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "html")))

    # Obtener el contenido de la página, incluyendo las etiquetas HTML
    page_content = driver.page_source

    # Traducir el contenido a idioma destino
    translated_content = translator.translate(page_content, dest=dest_language).text

    # Cerrar el driver
    driver.quit()

    # Escribir el contenido traducido en un nuevo archivo HTML
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(translated_content)

    print("Contenido traducido guardado en el archivo:", output_file_path)

# Ruta del archivo HTML
file_path = "./page.html"

# Idioma destino para la traducción
dest_language = "hi"

# Ruta del archivo de salida
output_file_path = "./page_translated.html"

# Llamar a la función para traducir la página web y guardar el contenido traducido en un archivo HTML
try:
    translate_web_page(file_path, dest_language, output_file_path)
except Exception as e:
    print("Error:", e)
