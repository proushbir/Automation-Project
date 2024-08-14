#Scroll page for Starbucks
import time

from selenium.webdriver.common.by import By


class ScrollPage:
    def __init__(self,driver):
        self.driver=driver
        self.link = (By.XPATH,"//a[normalize-space()='Learn more']")

    def open_gadgetbyte_page(self,url):
        self.driver.get(url)

    def scroll_home_page(self):
        # set the scroll parameter
        target_y = 3000
        scroll_distance = 1000
        current_y = 0

        # loop the scrolling
        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(1)

    def click_link(self):
        self.driver.find_element(*self.link).click()

    def scroll_learn_more_page(self):
        # set the scroll parameter
        target_y = 9000
        scroll_distance = 1000
        current_y = 0

        # loop the scrolling
        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(1)