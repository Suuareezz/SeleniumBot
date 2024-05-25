import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(8)

my_download_element = driver.find_element(By.ID, 'downloadButton')
my_download_element.click()

'''progress_element = driver.find_element(By.CLASS_NAME, 'progress-label')
print(progress_element.text == 'Complete!')'''

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        'Complete!'
    )
)
