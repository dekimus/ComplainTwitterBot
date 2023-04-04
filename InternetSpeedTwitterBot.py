from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class InternetSpeedTwitterBot:
    def __init__(self, up, down) -> None:
        self.up = up
        self.down = down
        self.Tup = ""
        self.Tdown = ""
        self.proveedor = "TU_PROVEEDOR_AQUI"
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options, service=Service(executable_path="c:\webdriver\chromedriver.exe", log_path="NUL"))
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        cookies = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookies.click()
        button=  self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        button.click()
        time.sleep(60)
        down = self.driver.find_element(By.CLASS_NAME, "download-speed")
        up = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.Tdown = down.text
        self.Tup = up.text
        self.driver.quit()
        self.driver1 = webdriver.Chrome(options=self.options, service=Service(executable_path="c:\webdriver\chromedriver.exe", log_path="NUL"))

    def tweet_at_provider(self, user, passw):
        self.driver1.get("https://www.twitter.com")
        time.sleep(1)
        login = self.driver1.find_element(By.CSS_SELECTOR, ".css-1dbjc4n a")
        login.click()
        time.sleep(1)
        text = self.driver1.find_element(By.NAME, "text")
        text.send_keys(f"{user}")
        time.sleep(0.5)
        text.send_keys(Keys.ENTER)
        time.sleep(1)
        text = self.driver1.find_element(By.NAME, "password")
        text.send_keys(f"{passw}")
        text.send_keys(Keys.ENTER)
        self.driver1.maximize_window()
        time.sleep(1)
        btt =  self.driver1.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        btt.send_keys(f"Hey {self.proveedor}, mi velocidad actual es {self.Tdown}/{self.Tup} y la contratada es {self.down}/{self.up}.Qué está pasando con la conexión?")
        time.sleep(20)
        
        