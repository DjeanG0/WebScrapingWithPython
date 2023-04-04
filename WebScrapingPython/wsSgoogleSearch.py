from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time

text = input("Indicame el texto a buscar -> ")
if text == "":
    text = 'josecodetech'


url = 'https://www.google.es/'
opciones = webdriver.ChromeOptions()
opciones.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='chromedriver', options=opciones)
driver.get(url)
driver.implicitly_wait(0.4)
try:
    accept_cookies = driver.find_element(
        by=By.XPATH, value='/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div')
    accept_cookies.click()
    print('Cookie aceptada')
    driver.implicitly_wait(1)
    search_box = driver.find_element(
        by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search_box.send_keys(text)
    # time.sleep(5)
    driver.implicitly_wait(1)
    print(f"Buscando el texto indicado = {text}")
    search_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(1)
    results = driver.find_elements(by=By.ID, value='search')
    for result in results:
        print(result.text)
except Exception as e:
    print(f'Ha ocurrido el error -> {e}')
finally:
    driver.implicitly_wait(1)
    driver.quit()