from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import booking.constants as consts
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Booking(webdriver.Chrome):
    def __init__(self, options: Options = None, service: Service = None, keep_alive: bool = True, teardown=False) -> None:
        super().__init__(options, service, keep_alive)
        self.teardown = teardown
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(consts.BASE_URL)

    def skip_pop(self):
        try:
            close_signinpopup = self.find_element(By.CSS_SELECTOR, 
            'button[aria-label="Dismiss sign-in info."]'
            )
            close_signinpopup.click()
        except:
            print('no signin popup')
        
    
    def select_place(self, dest=None):
        time.sleep(2)
        self.skip_pop()

        currency_elt = self.find_element(By.ID, 
            ':re:'
        )
        currency_elt.clear()
        currency_elt.send_keys(dest)
        time.sleep(2)

        clickfirstsugg = self.find_element(By.ID, 
            'autocomplete-result-0'
            )
        clickfirstsugg.click()
        time.sleep(5)

    def select_flexi_month(self, month):
        time.sleep(2)
        sel_flexitemp = self.find_element(By.XPATH,'//*[@id="indexsearch"]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[1]/ul/li[2]/button')
        sel_flexitemp.click()

        time.sleep(2)
        
        sel_month = self.find_element(By.XPATH, '//*[@id="flexible-searchboxdatepicker"]/div/div[1]/div[1]/div/div[2]/div[3]/label/span[2]')
        sel_month.click()
        time.sleep(1)

