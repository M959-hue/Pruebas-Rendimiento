# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestContrasea():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_contrasea(self):
    self.driver.get("http://localhost/home.php")
    self.driver.set_window_size(1279, 671)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("tolba@twitter.com")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("123456")
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    for i in range(1000):
      self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) strong").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".form-group:nth-child(1) > label"), "Email address"))
      self.driver.find_element(By.ID, "v-pills-profile-tab").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#v-pills-profile .form-group:nth-child(2) > label"), "Old Password"))
      self.driver.find_element(By.NAME, "old_password").click()
      self.driver.find_element(By.NAME, "old_password").send_keys("123456")
      self.driver.find_element(By.NAME, "new_password").click()
      self.driver.find_element(By.NAME, "new_password").send_keys("654321")
      self.driver.find_element(By.NAME, "ver_password").click()
      self.driver.find_element(By.NAME, "ver_password").send_keys("654321")
      self.driver.find_element(By.CSS_SELECTOR, ".text-center:nth-child(5) > .btn").click()
      self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) strong").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".form-group:nth-child(1) > label"), "Email address"))
      self.driver.find_element(By.ID, "v-pills-profile-tab").click()
      WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#v-pills-profile .form-group:nth-child(2) > label"), "Old Password"))
      self.driver.find_element(By.NAME, "old_password").click()
      self.driver.find_element(By.NAME, "old_password").send_keys("654321")
      self.driver.find_element(By.NAME, "new_password").click()
      self.driver.find_element(By.NAME, "new_password").send_keys("123456")
      self.driver.find_element(By.NAME, "ver_password").click()
      self.driver.find_element(By.NAME, "ver_password").send_keys("123456")
      self.driver.find_element(By.CSS_SELECTOR, ".text-center:nth-child(5) > .btn").click()

test = TestContrasea()
test.setup_method()
test.test_contrasea()
test.teardown_method()