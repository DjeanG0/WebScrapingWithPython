from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
def save_data(data):     #function to save data as csv file
    df = pd.DataFrame(data)
    df.to_csv('notices.csv')  
    print('saved data')


url = 'https://elcorreoweb.es'
opciones = webdriver.ChromeOptions()
opciones.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='chromedriver', options = opciones)
driver.get(url)
driver.implicitly_wait(0.4)

try:
    accept_cookies = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div/div[2]/div/button[2]')
    accept_cookies.click()
    notices_section = driver.find_element(
        by=By.XPATH, value='/html/body/div[2]/div/div[2]/div[1]/div/div[15]/div/section')
    notices = notices_section.find_elements(by=By.TAG_NAME, value='li')
    data = []
    for notice in notices:
        title = notice.find_element(by=By.CLASS_NAME, value='headline')
        web_link = title.find_element(by=By.TAG_NAME, value='a')
        link = web_link.get_attribute('href')
        title = web_link.text
        print(title)
        print(link)
        print('*'*50)
        driver.implicitly_wait(0.5)
        data_dic = {'title':title, 'link': link}
        data.append(data_dic)
    save_data(data)    #Use funtion to save data in csv
    for dato in data:
        print(f"Title':{dato['title']} \n Link : {dato['link']}\n")
except Exception as e:
    print(f'There was an error->{e}')
    
finally: 
    driver.implicitly_wait(0.5)
    driver.quit()
            