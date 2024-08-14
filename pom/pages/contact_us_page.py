#Contact Us Page for Nepal Education Consultancy
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ContactPage:
    def __init__(self,driver):
        self.driver=driver
        self.full_name = (By.XPATH,"//input[@placeholder='Full Name']")
        self.email_field = (By.XPATH, "//input[@placeholder='Email Id']")
        self.phone_field = (By.XPATH,"//input[@placeholder='Mobile Number']")
        self.education_dropdown = (By.XPATH,"//select[@name='education_level']")
        self.course_dropdown = (By.XPATH,"//select[@name='course']")
        self.percentage_field = (By.XPATH,"//input[@placeholder='Percentage']")
        self.select_country = (By.XPATH,"//input[@value='2']")
        self.submit_button = (By.XPATH,"//span[@class='btn-text']")

    def open_contact_page(self,url):
        self.driver.get(url)

    def enter_name(self,name):
        self.driver.find_element(*self.full_name).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def click_education(self):
        education = self.driver.find_element(*self.education_dropdown)
        Select(education).select_by_value("bachelor")

    def click_course(self):
        course = self.driver.find_element(*self.course_dropdown)
        Select(course).select_by_value("11")

    def enter_percentage(self,percentage):
        self.driver.find_element(*self.percentage_field).send_keys(percentage)

    def click_country(self):
        self.driver.find_element(*self.select_country).click()

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def is_valid_email(self,email):
        email_pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        return re.match(email_pattern, email) is not None

    def is_valid_phone(self,phone):
        return bool(re.match(r'^\d{10}$', phone))