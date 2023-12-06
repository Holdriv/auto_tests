from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))


try:
  link = "https://SunInJuly.github.io/execute_script.html"
  browser=webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
  x = x_element.text
  # print(x.text)
  y = calc(x)

  input = browser.find_element(By.ID, 'answer')
  input.send_keys(y)

  button = browser.find_element(By.TAG_NAME, "button")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)

  check= browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
  check.click()

  radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
  radio.click()

  button.click()
finally:
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()