from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = 'https://www.josecodetech.es'

opciones = webdriver.ChromeOptions() #Open web driver configuration

opciones.add_argument('--incognito')  # set chrome to incognito
driver = webdriver.Chrome(executable_path='chromedriver', options=opciones) #open browser since Chrome incognito

driver.get(url)
time.sleep(1)     #deley before next command
driver.close()

