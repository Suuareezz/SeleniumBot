from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://testpages.herokuapp.com/styled/calculator')
driver.implicitly_wait(8)

fname = driver.find_element(By.ID, 'number1')
lname = driver.find_element(By.ID, 'number2')
option = driver.find_element(By.ID, 'function')
ans = driver.find_element(By.ID, 'calculate')

fname.send_keys(12)
lname.send_keys(13)
selop = Select(option)
selop.select_by_visible_text('plus')
ans.click()

time.sleep(10)




