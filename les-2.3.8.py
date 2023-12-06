from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))
try:
  link = "http://suninjuly.github.io/explicit_wait2.html"
  browser=webdriver.Chrome()
  browser.get(link)
  button2 = browser.find_element(By.TAG_NAME, 'button')
  button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
  )
  button2.click()

  x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
  x = x_element.text
  y = calc(x)

  input = browser.find_element(By.ID, 'answer')
  browser.execute_script("return arguments[0].scrollIntoView(true);", input)
  input.send_keys(y)

  button3 = browser.find_element(By.ID, "solve")
  button3.click()
finally:
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()