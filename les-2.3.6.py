from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))


try:
  link = "http://suninjuly.github.io/redirect_accept.html"
  browser=webdriver.Chrome()
  browser.get(link)

  button = browser.find_element(By.TAG_NAME, 'button')
  button.click()

  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)

  time.sleep(2)

  x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
  x = x_element.text
  y = calc(x)

  input = browser.find_element(By.ID, 'answer')
  input.send_keys(y)

  button2 = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']")
  button2.click()
finally:
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()