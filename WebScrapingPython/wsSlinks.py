from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

url = 'https://www.josecodetech.es'

opciones = webdriver.ChromeOptions() #Open web driver configuration

opciones.add_argument('--incognito')  # set chrome to incognito
driver = webdriver.Chrome(executable_path='chromedriver', options=opciones) #open browser since Chrome incognito
driver.get(url)

titulo = driver.title  #obtain title
print(titulo)
print('*'*50)

cards = driver.find_elements(by=By.CLASS_NAME, value='card')  #obtain cards from web
for card in cards:
    print(card.text) 
print('*'*50)    

driver.implicitly_wait(0.1)

# obtain link of one card
card = driver.find_element(by=By.CLASS_NAME, value='card')
#print(card.text)
link = driver.find_element(by=By.XPATH, value='/html/body/main/div/div/div/div[1]/div/figure/a/img')
#print(link)
print('Changing of page.....')
driver.implicitly_wait(0.2)
link.click()
driver.implicitly_wait(0.2)
print('Come back to main page...')
driver.back()  #.refresh() or .forward()
driver.close()  #.quit() 

