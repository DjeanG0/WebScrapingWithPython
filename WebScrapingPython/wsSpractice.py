import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MiArañaSelenium:
    def __init__(self):
        self.start_urls = ["https://www.classcentral.com/"]
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)

    def start_requests(self):
        for url in self.start_urls:
            self.driver.get(url)
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "html"))
            )
            self.parse()

    def parse(self):
        html = self.driver.page_source

        # Save HTML in page.html file
        with open("page.html", "w") as f:
            f.write(html)
        # Obtain the CSS after the page has loaded
        css = self.driver.execute_script(
            """
            var css = '';
            var styles = document.getElementsByTagName('style');
            for (var i = 0; i < styles.length; i++) {
                css += styles[i].innerText + '\\n';
            }
            return css;
        """
        )

        # Save CSS in estilos.css file
        with open("style.css", "w") as f:
            f.write(css)

        # Download images and other resources
        assets_folder = "assets"
        for image in self.driver.find_elements(By.TAG_NAME, "img"):
            url = image.get_attribute("src")
            filename = url.split('/')[-1].split('?')[0]
            urllib.request.urlretrieve(url, assets_folder + filename)
        for link in self.driver.find_elements(By.CSS_SELECTOR, 'link[rel="icon"]'):
            url = link.get_attribute("href")
            filename = url.split("/links")[-1]
            urllib.request.urlretrieve(url, assets_folder + filename)

        print(css)

    def __del__(self):
        self.driver.quit()

if __name__ == '__main__':
    spider = MiArañaSelenium()
    spider.start_requests()