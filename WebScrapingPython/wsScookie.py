from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

url = 'https://www.josecodetech.es'

opciones = webdriver.ChromeOptions() #Open web driver configuration

opciones.add_argument('--incognito')  # set chrome to incognito
driver = webdriver.Chrome(executable_path='chromedriver', options=opciones) #open browser since Chrome incognito
driver.get(url)
driver.implicitly_wait(0.4)

try: 
    acccept_cookie = driver.find_element(by=By.XPATH, value='/html/body/footer/div/div[2]/button')
    acccept_cookie.click()
    print('Successfully clicked cookies')
    print(type(acccept_cookie))
    print(acccept_cookie)
except Exception as e:
    print(f'Error -> {e}')
finally:
    driver.quit()

