#Search and next page for Share Sansar

from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self,driver):
        self.driver=driver
        self.search_field = (By.XPATH, "//input[@id='company_search']")
        self.news = (By.XPATH, "//a[@id='btn_cnews']")
        self.page2 = (By.XPATH,"//a[normalize-space()='2']")
        self.page3 = (By.XPATH,"//a[normalize-space()='3']")

    def open_sharesansar_page(self,url):
        self.driver.get(url)

    def do_search(self,search):
        self.driver.find_element(*self.search_field).send_keys(search)

    def submit_search(self):
        self.driver.find_element(*self.search_field).submit()

    def click_news(self):
        self.driver.find_element(*self.news).click()

    def click_page2(self):
        self.driver.find_element(*self.page2).click()

    def click_page3(self):
        self.driver.find_element(*self.page3).click()