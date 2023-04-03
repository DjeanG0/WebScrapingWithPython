from selenium import webdriver
import time

url = 'https://www.josecodetech.es'

opciones = webdriver.ChromeOptions()

opciones.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='chromedriver', options=opciones) #open browser since Chrome incognito
time.sleep(1)
driver.get(url)
time.sleep(1)
driver.close()

