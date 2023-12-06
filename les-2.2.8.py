from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os



try:
  link = "http://suninjuly.github.io/file_input.html"
  browser=webdriver.Chrome()
  browser.get(link)


  input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
  input1.send_keys("Ivan")
  input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
  input2.send_keys("Petrov")
  input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
  input3.send_keys("@mail")

  current_dir = os.path.abspath(os.path.dirname(__file__))
  file_name = "example.txt"
  file_path = os.path.join(current_dir, file_name)

  element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
  element.send_keys(file_path)

  button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
  button.click()
finally:
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()