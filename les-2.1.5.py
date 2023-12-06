from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

try:
  link = "https://suninjuly.github.io/math.html"
  browser=webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
  x = x_element.text
  # print(x.text)
  y = calc(x)

  input = browser.find_element(By.ID, 'answer')
  input.send_keys(y)

  check= browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
  check.click()

  radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
  radio.click()

  button = browser.find_element(By.TAG_NAME, "button")
  button.click()
finally:
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()