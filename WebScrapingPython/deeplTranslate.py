from pydeepl import translate
from bs4 import BeautifulSoup

def translate_page(file_path, target_lang="ES"):
    # Leer el contenido del archivo HTML
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, "html.parser")
    body = soup.body

    # Divide el contenido del body en fragmentos de no más de 5000 caracteres
    fragments = [str(body)[i:i+5000] for i in range(0, len(str(body)), 5000)]

    # Traduce cada fragmento
    translated_fragments = []
    for fragment in fragments:
        translated_fragments.append(translate(fragment, to_lang=target_lang))

    # Une los fragmentos traducidos en un solo texto
    translated_content = ''.join(translated_fragments)

    # Guarda el contenido traducido en un nuevo archivo HTML
    output_file_path = file_path.split('.html')[0] + '_translated.html'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(translated_content)

    print("Contenido traducido guardado en el archivo:", output_file_path)

# Ruta del archivo HTML a traducir
file_path = "./page.html"

# Lenguaje destino para la traducción
target_lang = "ES"

# Llamar a la función para traducir la página y guardar el contenido traducido en un archivo HTML
translate_page(file_path, target_lang)
