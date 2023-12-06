from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
  link = "https://suninjuly.github.io/selects1.html"
  browser=webdriver.Chrome()
  browser.get(link)

  x1= browser.find_element(By.ID, 'num1').text
  x2= browser.find_element(By.ID, 'num2').text
  sum_x = int(x1)+int(x2)

  select = Select(browser.find_element(By.TAG_NAME, "select"))
  select.select_by_value(str(sum_x))

  button = browser.find_element(By.TAG_NAME, "button")
  button.click()
finally:
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()