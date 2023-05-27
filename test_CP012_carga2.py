import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestIngresoalsistemaerroneo():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_ingresoalsistemaerroneo(self):
        # Test name: Ingreso al sistema erroneo
        # Step # | name | target | value
        # 1 | open | https://tucan.toolsincloud.net/index.php |
        self.driver.get("http://localhost/index.php")
        # 2 | setWindowSize | 1361x684 |
        self.driver.set_window_size(1361, 684)

        email = "predetermiando@twitter.com"
        password = "clave123"

        for _ in range(300):  # Realizar 5 repeticiones
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
            # 8 | assertText | css=.span-fp-error | the email or password is not correct
            assert self.driver.find_element(By.CSS_SELECTOR, ".span-fp-error").text == "the email or password is not correct"
            # 9 | go refresh to login page
            self.driver.refresh()

if __name__ == '__main__':
    pytest.main([__file__])