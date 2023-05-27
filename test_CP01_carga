import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestIngresoalsistema():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_ingresoalsistema(self):
        # Test name: Ingreso al sistema
        # Step # | name | target | value
        # 1 | open | https://tucan.toolsincloud.net/index.php |
        self.driver.get("http://localhost/index.php")
        # 2 | setWindowSize | 1361x684 |
        self.driver.set_window_size(1361, 684)

        email = "tolba@twitter.com"
        password = "123456"

        for _ in range(200):  # Realizar repeticiones
            # 3 | click | name=email |
            self.driver.find_element(By.NAME, "email").click()
            # 4 | type | name=email | tolba@twitter.com
            self.driver.find_element(By.NAME, "email").send_keys(email)
            # 5 | click | name=password |
            self.driver.find_element(By.NAME, "password").click()
            # 6 | type | name=password | 123456
            self.driver.find_element(By.NAME, "password").send_keys(password)
            # 7 | click | name=login |
            self.driver.find_element(By.NAME, "login").click()

            # Realizar las acciones adicionales después de iniciar sesión
            # ...

            # 8 | go back to login page
            self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(11) strong").click()

test = TestIngresoalsistema()
test.setup_method()
test.test_ingresoalsistema()
test.teardown_method()
