import pytest
import time
import json
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

class TestCP041():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_cP041(self):
        print("Nombre de la prueba: Publicar un Squawk")
        print("Navegador: Chrome")
        success_count = 0
        failure_count = 0
        self.driver.get("http://localhost/home.php")
        # 2 | setWindowSize | 1382x744 |
        self.driver.set_window_size(1382, 744)
        self.driver.find_element(By.NAME, "email").click()
        # 4 | type | name=email | predeterminado.username@gmail.com
        self.driver.find_element(By.NAME, "email").send_keys("tolba@twitter.com")
        # 5 | click | name=password |
        self.driver.find_element(By.NAME, "password").click()
        # 6 | type | name=password | clave123
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        # 7 | sendKeys | name=password | ${KEY_ENTER}
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

       # message = "Hola TuCan esto es una prueba1 desde mi cuenta."
        #image_path = "prueba1.jpg"

        for _ in range(600):  # Realizar 5 repeticiones
            # Test name: CP04-1
            # Step # | name | target | value
            # 1 | open | /home.php |
            
            # 3 | click | name=status |
            self.driver.find_element(By.NAME, "status").click()
            # 4 | runScript | window.scrollTo(0,0) |
            self.driver.execute_script("window.scrollTo(0,0)")
            # 5 | type | name=status | Hola TuCan, esto es una prueba1 desde mi cuenta.
            self.driver.find_element(By.NAME, "status").send_keys("Esto es una prueba desde mi cuenta :)")
            # 6 | click | css=.fa-image |
           # self.driver.find_element(By.CSS_SELECTOR, ".fa-image").click()
            # 7 | type | id=tweet_img | C:\fakepath\prueba1.jpg
          #  self.driver.find_element(By.ID, "tweet_img").send_keys("prueba1.jpg")
            # 8 | click | id=tweet-input |
            self.driver.find_element(By.ID, "tweet-input").click()
            # 9 | close |  |
            if self.driver.current_url == "http://localhost/home.php":
                success_count += 1
                print(f"La prueba {success_count} fue exitosa")
            else:
                failure_count += 1
                print(f"La prueba {failure_count} fue fallida")
            self.driver.refresh()  # Actualizar la página para realizar la siguiente repetición

        self.driver.close()
        print("Ejecuta")

test = TestCP041()
test.setup_method()
test.test_cP041()